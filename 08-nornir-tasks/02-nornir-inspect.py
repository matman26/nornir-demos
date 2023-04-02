from nornir_inspect import nornir_inspect
from nornir.core.task import Task, Result
from nornir import InitNornir

def debug_task(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"Hello from {task.host.name}",
        failed=False,
        changed=False)

nr = InitNornir(config_file='config.yaml')
agg_results = nr.run(task=debug_task)

for host, result in agg_results.items():
    print(f"{host}: {result.result}")

nornir_inspect(agg_results)