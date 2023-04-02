from device_manager.helpers.json_helpers import nornir_result_to_dict
from device_manager.models import Device, DeviceGroup
from django.http import HttpResponse, HttpResponseRedirect
from nornir_netmiko.tasks import netmiko_send_command
from task_manager.models import ExecutionResults
from device_manager.manager.nornir import NornirMgr
from inspect import getmembers, isfunction
from django.shortcuts import render
import task_manager.custom.tasks as ct
import json

# Create your views here.
def run_task(request):
  mgr = NornirMgr()
  result = mgr.run_task(netmiko_send_command, command_string='show ip int brief')
  print(nornir_result_to_dict(result))
  return render(request, 'html/task_results.html', { 'results': result })

def run_command(request):
  if request.method == 'POST':
    name = request.POST['name']
    cmd = request.POST['command']
    mgr = NornirMgr()
    result = mgr.run_task(netmiko_send_command, command_string=cmd, name=name)
    return render(request, 'html/task_results.html',
                  { 'results': result })
  else:
    return render(request, 'html/send_command.html')

def custom_tasks(request):
  tasks = [ task[0] for task in getmembers(ct) if isfunction(task[1])]
  return render(request, 'html/show_custom_tasks.html',
                {'tasks': tasks})

def run_custom_task(request):
  def flatten_list(dictionary):
    # Copy the dictionary internally
    for k, v in dictionary.items():
      if isinstance(v, list):
        dictionary[k] = v[0]
    return dictionary

  if request.method == 'POST':
    taskname = request.POST['taskname']
    host_filter  = request.POST.getlist('hosts')
    group_filter = request.POST.getlist('groups')
    attributes = flatten_list(dict(request.POST))
    print(attributes)
    filter_expr = attributes['selection']

    attributes.pop('filter')

    print("EXPR IS")
    print(filter_expr)

    if host_filter:
      attributes.pop('hosts')
    if group_filter:
      attributes.pop('groups')

    selection = attributes.pop('selection')
    attributes.pop('taskname')
    attributes.pop('csrfmiddlewaretoken')
    curr_task = getattr(ct, taskname)
    mgr = NornirMgr()
    result = mgr.run_task(task_handle=curr_task, **flatten_list(attributes))
    return render(request, 'html/task_results.html',
                  { 'results': result })
  else:
    taskname = request.GET['taskname']
    curr_task = getattr(ct, taskname)
    task_vars = list(curr_task.__code__.co_varnames[:curr_task.__code__.co_argcount])
    task_vars.remove('task')
    return render(request, 'html/custom_form.html',
                  {
                    'taskvars': task_vars,
                    'task':     taskname,
                    'hosts': Device.objects.all(),
                    'groups': DeviceGroup.objects.all()
                   })


def results(request):
  result_id = request.GET['id']
  result_json = ExecutionResults.objects.get(pk=result_id)
  result = json.loads(result_json.results)
  return render(request, 'html/task_results.html',
                {'results': result })


def executions(request):
  ctx = {'results': ExecutionResults.objects.all()}
  return render(request, 'html/results_list.html', ctx)
