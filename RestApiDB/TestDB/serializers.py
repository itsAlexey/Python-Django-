from rest_framework.serializers import ModelSerializer

from .models import NetworkDevice, Interface, TrafficData#, ErrorLog##, 
# UserActivity,\
#     BandwidthUsage, DeviceConfiguration, AuthenticationLog, PerformanceMetrics, \
#     NetworkEvents, IPAddress, Configuration \
#     , DeviceTemperature, PowerConsumption, PacketLossData

# class UserActivitySerializer(ModelSerializer):
#     class Meta:
#         model = UserActivity
#         fields = '__all__'

# class DeviceConfigurationSerializer(ModelSerializer):
#     class Meta:
#         model = DeviceConfiguration
#         fields = '__all__'

# class BandwidthUsageSerializer(ModelSerializer):
#     class Meta:
#         model = BandwidthUsage
#         fields = '__all__'

# class AuthenticationLogSerializer(ModelSerializer):
#     class Meta:
#         model = AuthenticationLog
#         fields = '__all__'

# class PerformanceMetricsSerializer(ModelSerializer):
#     class Meta:
#         model = PerformanceMetrics
#         fields = '__all__'

class TrafficDataSerializer(ModelSerializer):
    class Meta:
        model = TrafficData
        fields = '__all__'

# class NetworkEventsSerializer(ModelSerializer):
#     class Meta:
#         model = NetworkEvents
#         fields = '__all__'

# class IPAddressSerializer(ModelSerializer):
#     class Meta:
#         model = IPAddress
#         fields = '__all__'

# class ConfigurationSerializer(ModelSerializer):
#     class Meta:
#         model = Configuration
#         fields = '__all__'

# class ErrorLogSerializer(ModelSerializer):
#     class Meta:
#         model = ErrorLog
#         fields = '__all__'

# class DeviceTemperatureSerializer(ModelSerializer):
#     class Meta:
#         model = DeviceTemperature
#         fields = '__all__'

# class PowerConsumptionSerializer(ModelSerializer):
#     class Meta:
#         model = PowerConsumption
#         fields = '__all__'

# class PacketLossDataSerializer(ModelSerializer):
#     class Meta:
#         model = PacketLossData
#         fields = '__all__'

class InterfaceSerializer(ModelSerializer):
    traffic_data = TrafficDataSerializer(many=True, read_only=True, source='trafficdata_set')
    class Meta:
        model = Interface
        fields = '__all__'

class NetworkDeviceSerializer(ModelSerializer):
    #AuthenticationLog, PerformanceMetrics, NetworkEvents, IPAddress, Configuration
    interfaces = InterfaceSerializer(many=True, read_only=True, source='interface_set')
    # error_logs = ErrorLogSerializer(many=True, read_only=True, source='errorlog_set')
    # user_activities = UserActivitySerializer(many=True, read_only=True, source='useractivity_set')
    # device_configurations = DeviceConfigurationSerializer(many=True, read_only=True, source='deviceconfiguration_set')
    # bandwidth_usage = BandwidthUsageSerializer(many=True, read_only=True, source='bandwidthusage_set')
    # authentication_log = AuthenticationLogSerializer(many=True, read_only=True, source='authenticationlog_set')
    # performance_metrics = PerformanceMetricsSerializer(many=True, read_only=True, source='performancemetrics_set')
    # network_events = NetworkEventsSerializer(many=True, read_only=True, source='networkevents_set')
    # ipaddress = IPAddressSerializer(many=True, read_only=True, source='ipaddress_set')
    # configurations = ConfigurationSerializer(many=True, read_only=True, source='configurations_set')
    # devicetemperature = DeviceTemperatureSerializer(many=True, read_only=True, source='devicetemperatures_set')
    # powerconsumption = PowerConsumptionSerializer(many=True, read_only=True, source='рowerсonsumptions_set')
    # packetlossdata = PacketLossDataSerializer(many=True, read_only=True, source='packetlossdatas_set')
    
    class Meta:
        model = NetworkDevice
        fields = '__all__'