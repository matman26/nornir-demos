from django.db import models
from django.forms import ModelForm

class DeviceAttributes(models.Model):
  """
      Template (abstract) class for devices, device-groups and defaults
  """
  # Fields need to be nullable to behave according to nornir's
  # inventory inheritance model
  hostname           = models.CharField('device fqdn or ip address', max_length=255, default=None, blank=True, null=True)
  username           = models.CharField('device username', max_length=255, default=None, blank=True, null=True)
  password           = models.CharField('device password', max_length=255, default=None, blank=True, null=True)
  platform           = models.CharField('device platform', max_length=255, default=None, blank=True, null=True)
  port               = models.IntegerField('ssh port number', default=None, blank=True, null=True)
  connection_options = models.TextField('connection options (json-formatted)', default=None, blank=True,null=True)
  data               = models.TextField('free-form data (json-formatted)', default=None, blank=True,null=True)

  class Meta:
    abstract = True

# Create your models here.
class Device(DeviceAttributes):
  # Nornir enforces that device names be unique, so it makes sense to use
  # names as primary keys
  name   = models.CharField('device name', primary_key=True, max_length=255)
  groups = models.CharField('device groups (comma-separated)', max_length=255, default=None, blank=True, null=True)
  class Meta:
    db_table = 'devices'
    managed  = True

class DeviceGroup(DeviceAttributes):
  # Nornir enforces that group names be unique, so it makes sense to use
  # names as primary keys
  name   = models.CharField('group name', primary_key=True, max_length=255)
  groups = models.CharField('device groups (comma-separated)', max_length=255, default=None, blank=True, null=True)
  class Meta:
    db_table = 'groups'
    managed  = True

class Defaults(DeviceAttributes):
  class Meta:
    db_table = 'defaults'
    managed  = True



