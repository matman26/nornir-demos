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
