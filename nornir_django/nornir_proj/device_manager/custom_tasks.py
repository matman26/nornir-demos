from nornir.core.task import Result

def newtask(task):
  res = f'Hello host {task.host}'
  return Result(
    host=task.host,
    result=res,
    changed=False
  )
