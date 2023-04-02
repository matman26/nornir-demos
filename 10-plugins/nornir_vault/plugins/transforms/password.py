from nornir.core.inventory import Host
from cryptography.fernet import Fernet
from os import getenv

def decrypt_password(host: Host):
  key = getenv('NR_DECRYPT_PASSWORD')
  if key == None:
    print("Please set the NR_DECRYPT_PASSWORD environment variable for this execution")
    raise Exception("NRPasswordNotDefined")
  f = Fernet(bytes(key,'utf-8'))
  encrypted_password = host.password
  host.password = f.decrypt(bytes(encrypted_password,'utf-8')).decode()
