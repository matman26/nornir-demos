from napalm import get_network_driver

devices = (
    {
      "hostname": "10.0.2.1",
      "username": "cisco",
      "password": "cisco",
      "optional_args": {'secret': 'cisco'}
    },
    {
      "hostname": "10.0.2.2",
      "username": "cisco",
      "password": "cisco",
      "optional_args": {'secret': 'cisco'}
    })

driver = get_network_driver('ios')
for device in devices:
    connection = driver(**device)
    connection.open()
    version = connection.get_facts()['os_version']
    print(f"OS Version for device {device['hostname']} is {version}")
    serial = connection.get_facts()['serial_number']
    print(f"Serial number for device {device['hostname']} is {serial}")
    connection.close()


