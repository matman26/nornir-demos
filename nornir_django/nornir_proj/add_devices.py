from device_manager.models import DeviceModel
for i in range(6, 22):
  t = DeviceModel(name=f'R{i}', hostname=f'192.168.12.{i}', username='cisco', password='cisco', platform='cisco_ios', port=22)
  t.save()




