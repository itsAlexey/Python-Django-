from django.contrib import admin
from .models import NetworkDevice, Interface, TrafficData, ErrorLog, TypeDevices #UserActivity, \
    #BandwidthUsage, DeviceConfiguration, AuthenticationLog, PerformanceMetrics, NetworkEvents, \
    #IPAddress, Configuration, DeviceTemperature, PowerConsumption,  PacketLossData, Users, , HostDevice
# Register your models here.

admin.site.register(NetworkDevice)
admin.site.register(Interface)
admin.site.register(TrafficData)
admin.site.register(ErrorLog)
# admin.site.register(UserActivity)
# admin.site.register(BandwidthUsage)
# admin.site.register(DeviceConfiguration)
# admin.site.register(AuthenticationLog)
# admin.site.register(PerformanceMetrics)
# admin.site.register(NetworkEvents)
# admin.site.register(IPAddress)
# admin.site.register(Configuration)
# admin.site.register(DeviceTemperature)
# admin.site.register(PowerConsumption)
# admin.site.register(PacketLossData)
# admin.site.register(Users)
admin.site.register(TypeDevices)
# admin.site.register(HostDevice)