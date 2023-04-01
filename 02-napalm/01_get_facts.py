from napalm import get_network_driver

device = {
  "hostname": "10.0.2.1",
  "username": "cisco",
  "password": "cisco",
  "optional_args": {'secret': 'cisco'}
}

driver = get_network_driver('ios')
connection = driver(**device)

connection.open()
running_config = connection.get_config()['running']
print(running_config)


