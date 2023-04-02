from nornir import InitNornir
from nornir.core.plugins.runners import RunnersPluginRegister
from plugins.runners.progressbar import ThreadedProgressBarRunner
from nornir.core.plugins.inventory import InventoryPluginRegister
from nornir_csv.plugins.inventory import CsvInventory
from nornir.core.task import Task, Result
from time import sleep
from random import randint

def hello_world(task: Task) -> Result:
  sleep(randint(0,6))
  return Result(
    result=f"Hello {task.host}",
    host=task.host,
    changed=False,)

RunnersPluginRegister.register("ProgressBar", ThreadedProgressBarRunner)
InventoryPluginRegister.register("CsvInventory", CsvInventory)

nr = InitNornir(config_file="config.yaml")
results = nr.run(task=hello_world)
