import gdb

class InfoKtasks(gdb.Command):
  """Show kernel task list."""

  def __init__(self):
    super(InfoKtasks, self).__init__("info ktasks", gdb.COMMAND_STATUS)

  def invoke(self, arg, from_tty):
    t_long = gdb.lookup_type("long")
    t_task = gdb.lookup_type("struct task_struct")
    init = gdb.parse_and_eval("init_task")
    offset = init["tasks"].address.cast(t_long) - init.address.cast(t_long)
    task = init.address
    print("{0:>5} {1:}".format("PID", "COMM"))
    while True:
      print("{0:>5} {1:}".format(str(task["pid"]),
                                 task["comm"].string()))
      task = (task["tasks"]["next"].cast(t_long) - offset).cast(t_task.pointer())
      if task == init.address:
        break

InfoKtasks()
