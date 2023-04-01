from scrapli import Scrapli
from scrapli_cfg import ScrapliCfg

device = {
   "host": "sandbox-iosxr-1.cisco.com",
   "auth_username": "admin",
   "auth_password": "C1sco12345",
   "auth_secondary": "cisco",
   "auth_strict_key": False,
   "platform": "cisco_iosxr",
   "ssh_config_file": "/home/augustus/.ssh/config"
}

with open("config.txt", "r") as f:
    my_config = f.read()

with Scrapli(**device) as conn:
  cfg_conn = ScrapliCfg(conn=conn)
  cfg_conn.prepare()
  cfg_conn.load_config(config=my_config, replace=True)
  diff = cfg_conn.diff_config()
  print(diff.side_by_side_diff)
  cfg_conn.commit_config()
  cfg_conn.cleanup()
