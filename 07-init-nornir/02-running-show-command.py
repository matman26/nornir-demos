from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_command
from nornir import InitNornir

nr = InitNornir(
	inventory={
	  'plugin': 'SimpleInventory',
	  'options': {
	    'host_file': "hosts.yaml"
	  }
	},
	runner={
	  'plugin': 'threaded',
	  'options': {
	    'num_workers': 20 
	  }
	})

result = nr.run(task=netmiko_send_command, command_string="show ip route")
print_result(result)
