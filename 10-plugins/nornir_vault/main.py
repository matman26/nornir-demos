from nornir.core.plugins.inventory import TransformFunctionRegister
from plugins.transforms.password import decrypt_password
from nornir import InitNornir

TransformFunctionRegister.register('decrypt_password', decrypt_password)

nr = InitNornir(config_file='config.yaml')
print(f"Decrypted password is: {nr.inventory.hosts['R1'].password}")
