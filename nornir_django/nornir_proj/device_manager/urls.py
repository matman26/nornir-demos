from django.urls import path

from . import views

urlpatterns = [
    path('devices',     views.devices,       name='devices'),
    path('groups',      views.groups,        name='groups'),
    path('defaults',    views.defaults,      name='defaults'),
    path('add-device',  views.add_device,    name='add_device'),
    path('edit-device', views.edit_device,   name='edit_device'),
    path('add-group',   views.add_group,     name='add_group'),
    path('set-defaults',views.set_defaults,  name='set_defaults'),
    path('remove',      views.remove_device, name='remove_device'),
]

