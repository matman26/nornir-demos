from nornir.core.task import Task, Result
import json

def debug_task(task: Task) -> Result:
    results_dict = {
        'name': task.host.name,
        'hostname': task.host.hostname,
        'username': task.host.username,
        'password': task.host.password,
        'platform': task.host.platform,
        'port': task.host.port,
        'data': task.host.data,
    }
    return Result(
        name='debug',
        changed=False,
        host=task.host,
        failed=False,
        result=json.dumps(results_dict))

def hello_task(task: Task) -> Result:
    return Result(
        name='hello',
        changed=False,
        host=task.host,
        failed=False,
        result=f"Hello from {task.host.name}!")

def task_with_args(task: Task, user_input: str ) -> Result:
    return Result(
        name='args',
        changed=False,
        host=task.host,
        failed=False,
        result=f"Hello from {task.host.name}! Input was {user_input}.")

def task_with_subtask(task: Task) -> Result:
    task.run(task=debug_task)
    task.run(task=hello_task)

    return Result(
        result='Finished task with subtasks',
        host=task.host,
        changed=False,
        failed=False
    )

def toto_tata(task: Task) -> Result:
    print('entrando na tarefa')
