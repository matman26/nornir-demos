from nornir import InitNornir

nr = InitNornir(
	inventory={
	  'plugin': 'SimpleInventory',
	  'options': {
	    'host_file': "filtering/hosts.yaml",
	    'group_file': "filtering/groups.yaml"
	  }
	},
	runner={
	  'plugin': 'threaded',
	  'options': {
	    'num_workers': 20 
	  }
	})

print(f"Inventory contains {len(nr.inventory.hosts)} hosts")
print(nr.inventory.hosts.keys())