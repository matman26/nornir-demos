from scrapli import Scrapli

device = {
   "host": "sandbox-iosxr-1.cisco.com",
   "auth_username": "admin",
   "auth_password": "C1sco12345",
   "auth_secondary": "cisco",
   "auth_strict_key": False,
   "platform": "cisco_iosxr",
   "ssh_config_file": "/home/augustus/.ssh/config"
}

conn = Scrapli(**device)
conn.open()
print("Found prompt:")
print(conn.get_prompt())

print("Running 'show running-config'")
res = conn.send_command('show running-config')
print(res.result)

config = res.result
choice = input("Would you like to save this configuration? [y/N] ")
if choice in ('y', 'Y'):
    with open('config.txt','w') as f:
        f.write(config)
        

