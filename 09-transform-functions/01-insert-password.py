from nornir.core.plugins.inventory import TransformFunctionRegister
from nornir.core.task import Task, Result
from nornir.core.inventory import Host
from nornir import InitNornir
from getpass import getpass

def debug_task(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"Hello world from {task.host.name}",
        failed=False,
        changed=False)

def insert_password(host: Host, password: str) -> None:
    host.password = password

TransformFunctionRegister.register('insert_password', insert_password)

nr = InitNornir(
	inventory={
	  'plugin': 'SimpleInventory',
	  'options': {
	    'host_file': "hosts.yaml"
	  },
      'transform_function': 'insert_password',
      'transform_function_options': {
        'password': getpass()
      }
	},
	runner={
	  'plugin': 'threaded',
	  'options': {
	    'num_workers': 20 
	  }
	})


print("name", "hostname", "username", "password")
for host, data in nr.inventory.hosts.items():
    print(host, data.hostname, data.username, data.password)