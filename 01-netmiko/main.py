from netmiko import ConnectHandler

device = {
  "device_type": "cisco_ios",
  "host": "10.0.2.1",
  "username": "cisco",
  "password": "cisco",
  "secret": "cisco",
}

net_connect = ConnectHandler(**device)
output = net_connect.send_command("show ip interface brief")

print(output)