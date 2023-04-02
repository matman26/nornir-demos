from nornir.core.plugins.inventory import InventoryPluginRegister
from nornir.core.processor import Processors
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_command
from device_manager.django_inventory import  DjangoInventory
from device_manager.custom_processor import DjangoEventProcessor
from device_manager.custom_processor import DjangoResultProcessor
from nornir.core.task import Task, Result
import device_manager.custom_tasks as ct
from nornir import InitNornir
from sys import modules

class FilterObj():
  def __init__(self):
    pass

class NornirMgr():
  def __init__(self):
    InventoryPluginRegister.register("DjangoInventory", DjangoInventory)

    self.nr = InitNornir(
      inventory = {
        'plugin': 'DjangoInventory'
      },
      runner = {
        'plugin': 'threaded',
        'options': {
          'num_workers': 20
        }
      },
    )

    self.nr = self.nr.with_processors([DjangoEventProcessor(), DjangoResultProcessor()])

  def run_task(self, task_handle: Task, *args, **kwargs) -> Result:
    return self.nr.run(task=task_handle, *args, **kwargs)

  def run_tasklist(self, tasklist) -> Result:
    """
        Tasklist is [
	   ('task_a', {'arg_a_task_a' : 'toto' }),
	   ('task_b', {'arg_a_task_b' : 'tata' })
       ]
    """
    for task, kwargs in tasklist:
      task_handle = getattr(ct, task)
      self.nr.run(task=task_handle,  **kwargs)

