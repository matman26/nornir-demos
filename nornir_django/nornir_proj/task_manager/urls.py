from django.urls import path

from . import views

urlpatterns = [
    path('index',        views.run_task,      name='index'),
    path('show-result',  views.results,       name='show_result'),
    path('run-task',     views.run_task,      name='run_task'),
    path('custom-tasks', views.custom_tasks,  name='custom_task'),
    path('run-custom-tasks', views.run_custom_task,  name='run_custom'),
    path('send-command', views.run_command,   name='run_command'),
    path('executions',   views.executions,    name='executions'),
    path('events',       views.run_task,      name='executions'),
]
