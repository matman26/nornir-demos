from django.contrib import admin
from device_manager.models import Defaults
from device_manager.models import Device
from device_manager.models import DeviceGroup

# Register your models here.

@admin.register(Device)
class DeviceModelAdmin(admin.ModelAdmin):
    pass

@admin.register(DeviceGroup)
class DeviceGroupModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Defaults)
class MyModelAdmin(admin.ModelAdmin):
    # Defaults table should only have a single instance
    def has_add_permission(self, request):
        return not Defaults.objects.exists()
