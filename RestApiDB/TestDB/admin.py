from django.contrib import admin
from .models import TypeDevices, HostDevice, NetworkDevice, Interface, TrafficData, BandwidthUsage, \
NetworkEvents, DeviceTemperature, PowerConsumption, DeviceConfiguration, PerformanceMetrics, IPAddress, \
PacketLossData, User, UserActivity, AuthenticationLog
# Register your models here.

admin.site.register(NetworkDevice)
admin.site.register(Interface)
admin.site.register(TrafficData)
admin.site.register(User)
admin.site.register(UserActivity)
admin.site.register(BandwidthUsage)
admin.site.register(DeviceConfiguration)
admin.site.register(AuthenticationLog)
admin.site.register(PerformanceMetrics)
admin.site.register(NetworkEvents)
admin.site.register(IPAddress)
admin.site.register(DeviceTemperature)
admin.site.register(PowerConsumption)
admin.site.register(PacketLossData)
admin.site.register(TypeDevices)
admin.site.register(HostDevice)
