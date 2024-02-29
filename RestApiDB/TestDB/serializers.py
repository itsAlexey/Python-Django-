from rest_framework.serializers import ModelSerializer

from .models import TypeDevices, HostDevice, NetworkDevice, Interface, TrafficData, BandwidthUsage, \
NetworkEvents, DeviceTemperature, PowerConsumption, DeviceConfiguration, PerformanceMetrics, IPAddress, \
PacketLossData, User, UserActivity, AuthenticationLog

class TypeDevicesSerializer(ModelSerializer):
    class Meta:
        model = TypeDevices
        fields = '__all__'

class HostDeviceSerializer(ModelSerializer):
    class Meta:
        model = HostDevice
        fields = '__all__'

class NetworkDeviceSerializer(ModelSerializer):
    class Meta:
        model = NetworkDevice
        fields = '__all__'

class TrafficDataSerializer(ModelSerializer):
    class Meta:
        model = TrafficData
        fields = '__all__'

class BandwidthUsageSerializer(ModelSerializer):
    class Meta:
        model = BandwidthUsage
        fields = '__all__'

class NetworkEventsSerializer(ModelSerializer):
    class Meta:
        model = NetworkEvents
        fields = '__all__'

class DeviceTemperatureSerializer(ModelSerializer):
    class Meta:
        model = DeviceTemperature
        fields = '__all__'

class PowerConsumptionSerializer(ModelSerializer):
    class Meta:
        model = PowerConsumption
        fields = '__all__'

class DeviceConfigurationSerializer(ModelSerializer):
    class Meta:
        model = DeviceConfiguration
        fields = '__all__'

class PerformanceMetricsSerializer(ModelSerializer):
    class Meta:
        model = PerformanceMetrics
        fields = '__all__'

class IPAddressSerializer(ModelSerializer):
    class Meta:
        model = IPAddress
        fields = '__all__'

class PacketLossDataSerializer(ModelSerializer):
    class Meta:
        model = PacketLossData
        fields = '__all__'

class UserActivitySerializer(ModelSerializer):
    class Meta:
        model = UserActivity
        fields = '__all__'

class AuthenticationLogSerializer(ModelSerializer):
    class Meta:
        model = AuthenticationLog
        fields = '__all__'

class UserSerializer(ModelSerializer):
    User_Activity = UserActivitySerializer(many=True, read_only=True, source='user_activity_set')
    Authentication_Log = AuthenticationLogSerializer(many=True, read_only=True, source='authentication_log_set')
    class Meta:
        model = User
        fields = '__all__'

class InterfaceSerializer(ModelSerializer):
    traffic_data = TrafficDataSerializer(many=True, read_only=True, source='trafficdata_set')
    Bandwidth_Usage = BandwidthUsageSerializer(many=True, read_only=True, source='bandwidth_usage_set')
    class Meta:
        model = Interface
        fields = '__all__'

class NetworkDeviceSerializer(ModelSerializer):
    interfaces = InterfaceSerializer(many=True, read_only=True, source='interface_set')
    Network_Events = NetworkEventsSerializer(many=True, read_only=True, source='network_events_set')
    Device_Temperature = DeviceTemperatureSerializer(many=True, read_only=True, source='device_temperature_set')
    Power_Consumption = PowerConsumptionSerializer(many=True, read_only=True, source='рower_сonsumption_set')
    Device_Configuration = DeviceConfigurationSerializer(many=True, read_only=True, source='device_configuration_set')
    Performance_Metrics = PerformanceMetricsSerializer(many=True, read_only=True, source='performance_metrics_set')
    IPAddress_data = IPAddressSerializer(many=True, read_only=True, source='ip_address_set')
    PacketLoss_Data = PacketLossDataSerializer(many=True, read_only=True, source='packetloss_data_set')
    
    class Meta:
        model = NetworkDevice
        fields = '__all__'
