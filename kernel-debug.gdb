define ktasks
  set $offset = (long)&init_task.tasks - (long)&init_task
  set $task = &init_task
  printf "  PID COMM\n"
  while 1
    printf "%5d %s\n", $task->pid, $task->comm
    set $task = (struct task_struct *)((long)$task->tasks.next - $offset)
    if $task == &init_task
      loop_break
    end
  end
end
document ktasks
Show kernel task list.
end
