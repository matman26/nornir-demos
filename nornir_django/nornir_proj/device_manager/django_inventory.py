from nornir.core.inventory import Inventory, ParentGroups
from nornir.core.inventory import ConnectionOptions
from nornir.core.inventory import BaseAttributes
from nornir.core.inventory import HostOrGroup
from nornir.core.inventory import Defaults
from nornir.core.inventory import Groups
from nornir.core.inventory import Group
from nornir.core.inventory import Hosts
from nornir.core.inventory import Host
from typing import Dict, Any, Type
from .models import DeviceGroup
from .models import Defaults
from .models import Device
import json

# Shamelessly copied from SimpleInventory
def _get_connection_options(data: Dict[str, Any]) -> Dict[str, ConnectionOptions]:
  cp = {}
  for cn, c in data.items():
    cp[cn] = ConnectionOptions(
        hostname=c.get("hostname"),
        port=c.get("port"),
        username=c.get("username"),
        password=c.get("password"),
        platform=c.get("platform"),
        extras=c.get("extras"),
    )

  return cp

def _get_defaults(defaults_dict: Dict[str, Any]) -> Defaults:
  return Defaults(
      hostname=defaults_dict.get("hostname"),
      port=defaults_dict.get("port"),
      username=defaults_dict.get("username"),
      password=defaults_dict.get("password"),
      platform=defaults_dict.get("platform"),
      data=defaults_dict.get("data"),
      connection_options=_get_connection_options(defaults_dict.get("connection_options")),
  )


def _get_inventory_element(
    typ: Type[HostOrGroup], data: Dict[str, Any], name: str, defaults: Defaults
) -> HostOrGroup:
    return typ(
        name=name,
        hostname=data.get("hostname"),
        port=data.get("port"),
        username=data.get("username"),
        password=data.get("password"),
        platform=data.get("platform"),
        data=data.get("data"),
        groups=data.get(
            "groups"
        ),  # this is a hack, we will convert it later to the correct type
        defaults=defaults,
        connection_options=_get_connection_options(data.get("connection_options", {})),
    )


def get_fields_as_dict(deviceObject: Device) -> Dict:
  attributes = ('name', 'hostname', 'username', 'password', 'platform', 'port')
  fields     = dict()

  # Process Regular attributes
  for field in attributes:
    fields[field] = getattr(deviceObject, field)

  fields['groups'] = []
  # Split groups coming from DB as a python list
  groups = deviceObject.groups.split(',')
  if groups not in (None, ''):
    for group in deviceObject.groups.split(','):
      fields['groups'].append(group)

  # Connection options stuff and data are both json objs
  for attr in ('connection_options', 'data'):
    data = getattr(deviceObject, attr)
    fields[attr] =  json.loads(data) if data not in (None, '')  else {}

  return fields

def get_defaults_as_dict(defaultsObject: Defaults) -> Dict:
  attributes = ('hostname', 'username', 'password', 'platform', 'port')
  fields     = dict()

  # Process Regular attributes
  for field in attributes:
    fields[field] = getattr(defaultsObject, field)

  # Connection options stuff and data are both json objs
  for attr in ('connection_options', 'data'):
    data = getattr(defaultsObject, attr)
    fields[attr] =  json.loads(data) if data not in (None, '')  else {}

  return fields

class DjangoInventory:
  def __init__(self) -> None:
    self.devices = Device.objects.all() # QuerySet
    self.groups  = DeviceGroup.objects.all()
    self.defaults = Defaults.objects.all()

  def load(self) -> Inventory:
    if not self.defaults:
      defaults = _get_defaults({})
    else:
      defaults = _get_defaults(get_defaults_as_dict(self.defaults[0]))

    hosts_dict = { f"{device.name}": get_fields_as_dict(device) for device in self.devices }
    hosts = Hosts()
    for n,h in hosts_dict.items():
      hosts[n] = _get_inventory_element(Host, h, n, defaults)

    groups = Groups()
    if self.groups != None:
      groups_dict = { f"{group.name}": get_fields_as_dict(group) for group in self.groups }
      for n, g in groups_dict.items():
        groups[n] = _get_inventory_element(Group, g, n, defaults)

      for g in groups.values():
        g.groups = ParentGroups([groups[g] for g in g.groups if g != ''])

    for h in hosts.values():
      h.groups = ParentGroups([groups[g] for g in h.groups if g != ''])

    return Inventory(hosts=hosts, groups=groups, defaults=defaults)

