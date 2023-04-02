from nornir.core.task import Task, Result
from nornir_inspect import nornir_inspect
from nornir import InitNornir

def debug_task(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name}: {task.host.hostname}")

def hello_task(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"Hello from {task.host.name}")

def supertask(task: Task):
    task.run(debug_task)
    task.run(hello_task)

    return Result(
        host=task.host,
        result="Result from supertask")


nr = InitNornir(config_file='config.yaml')
all_results = nr.run(supertask)
nornir_inspect(all_results)
