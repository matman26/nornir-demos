from device_manager.models import Device, DeviceGroup, Defaults
from device_manager.forms import DeviceForm, GroupForm, DefaultsForm
from device_manager.helpers.json_helpers import nornir_result_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from device_manager.manager.nornir import NornirMgr
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.template import loader

# Create your views here.
def devices(request):
  devices_list = Device.objects.all()
  template     = loader.get_template('html/devices.html')
  context = {
    'devices_list': devices_list
  }
  return HttpResponse(template.render(context, request))

def groups(request):
  groups_list = DeviceGroup.objects.all()
  template     = loader.get_template('html/groups.html')
  context = {
    'groups_list': groups_list
  }
  return HttpResponse(template.render(context, request))

def defaults(request):
  defaults_list = Defaults.objects.all()
  template     = loader.get_template('html/defaults.html')
  context = {
    'defaults': defaults_list[0]
  }
  return HttpResponse(template.render(context, request))

def add_device(request):
  if request.method == 'POST':
    form_data = DeviceForm(request.POST)
    if form_data.is_valid():
      form_data.save()
      return HttpResponseRedirect('/device-manager/devices')
  else:
    form_data =  DeviceForm()
    return render(request, 'html/add_device_form.html',
                  { 'form': form_data,
                    'post': '/device-manager/add-device' })

def edit_device(request):
  if request.method == 'POST':
    # If its a post, accept incoming data
    name = request.POST['name']
    device = Device.objects.get(pk=name)
    form_data = DeviceForm(request.POST, instance=device)
    if form_data.is_valid():
      form_data.save()
      return HttpResponseRedirect('/device-manager/devices')
  else:
    # If its a get, prepopulate the form
    # with current data
    name   = request.GET['name']
    device = Device.objects.get(pk=name)
    if device:
      form_data = DeviceForm(initial=model_to_dict(device))
      return render(request, 'html/add_device_form.html',
                     { 'form': form_data,
                       'post': '/device-manager/edit-device'})

def add_group(request):
  if request.method == 'POST':
    form_data = GroupForm(request.POST)
    if form_data.is_valid():
      form_data.save()

    return HttpResponseRedirect('/device-manager/groups')
  else:
    form_data =  GroupForm()
    return render(request, 'html/add_group_form.html',
                  { 'form': form_data })

def remove_device(request):
  name = dict(request.GET)['name'][0]
  try:
    device = Device.objects.get(pk=name)
    device.delete()
  except Device.DoesNotExist:
    print(f'Request for device {name} is invalid.')

  return HttpResponseRedirect('/device-manager/devices')

def set_defaults(request):
  defaults = Defaults.objects.all()
  if request.method == 'POST':
    if defaults:
      form_data = DefaultsForm(request.POST, instance=defaults[0])
    else:
      form_data = DefaultsForm(request.POST)
    if form_data.is_valid():
      form_data.save()
      return HttpResponseRedirect('/device-manager/devices')
  else:
    if defaults:
      form_data = DefaultsForm(initial=model_to_dict(defaults[0]))
    else:
      form_data =  DefaultsForm()
    return render(request, 'html/set_defaults_form.html',
                  { 'form': form_data })
