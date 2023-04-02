from device_manager.models import Device, DeviceGroup, Defaults
from django.forms import ModelForm
from django import forms

class AttributesForm(ModelForm):
  hostname =  forms.CharField(widget=forms.TextInput(attrs={'class': 'w3-input'}))
  username =  forms.CharField(widget=forms.TextInput(attrs={'class': 'w3-input'}))
  password =  forms.CharField(widget=forms.TextInput(attrs={'class': 'w3-input'}))
  platform =  forms.CharField(widget=forms.TextInput(attrs={'class': 'w3-input'}))
  port     =  forms.IntegerField(widget=forms.TextInput(attrs={'class': 'w3-input'}))
  data     =  forms.CharField(widget=forms.Textarea(attrs={"class": "w3-input"}))
  connection_options =  forms.CharField(widget=forms.Textarea(attrs={"class": "w3-input"}))

  def __init__(self, *args, **kwargs):
    super(AttributesForm, self).__init__(*args, **kwargs)
    self.fields['hostname'].required = False
    self.fields['username'].required = False
    self.fields['password'].required = False
    self.fields['platform'].required = False
    self.fields['port'].required = False
    self.fields['data'].required = False
    self.fields['connection_options'].required = False

  class Meta:
    abstract = True

class DeviceForm(AttributesForm):
  name     =  forms.CharField(widget=forms.TextInput(attrs={'class': 'w3-input'}))
  groups   =  forms.CharField(widget=forms.TextInput(attrs={'class': 'w3-input'}))

  def __init__(self, *args, **kwargs):
    super(DeviceForm, self).__init__(*args, **kwargs)
    self.fields['groups'].required = False

  class Meta:
    model  = Device
    fields = [
      'name',
      'hostname',
      'username',
      'password',
      'platform',
      'port',
      'groups',
      'data',
      'connection_options',
    ]

class GroupForm(AttributesForm):
  name     =  forms.CharField(widget=forms.TextInput(attrs={'class': 'w3-input'}))
  groups   =  forms.CharField(widget=forms.TextInput(attrs={'class': 'w3-input'}))

  def __init__(self, *args, **kwargs):
    super(GroupForm, self).__init__(*args, **kwargs)
    self.fields['groups'].required = False

  class Meta:
    model  = DeviceGroup
    fields = [
      'name',
      'hostname',
      'username',
      'password',
      'platform',
      'port',
      'groups',
      'data',
      'connection_options',
    ]

class DefaultsForm(AttributesForm):
  class Meta:
    model  = Defaults
    fields = [
      'hostname',
      'username',
      'password',
      'platform',
      'port',
      'data',
      'connection_options',
    ]
