from rest_framework.serializers import ModelSerializer, SerializerMethodField

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
    User_Activity = UserActivitySerializer(many=True, read_only=True, source='useractivity_set')
    Authentication_Log = AuthenticationLogSerializer(many=True, read_only=True, source='authenticationlog_set')
    class Meta:
        model = User
        fields = '__all__'

class InterfaceSerializer(ModelSerializer):
    traffic_data = TrafficDataSerializer(many=True, read_only=True, source='trafficdata_set')
    Bandwidth_Usage = BandwidthUsageSerializer(many=True, read_only=True, source='bandwidthusage_set')
    class Meta:
        model = Interface
        fields = '__all__'

class NetworkDeviceSerializer(ModelSerializer):
    Type_device = TypeDevicesSerializer(many=True, read_only=True, source='type_network_device')
    interfaces = InterfaceSerializer(many=True, read_only=True, source='interface_set')
    Network_Events = NetworkEventsSerializer(many=True, read_only=True, source='networkevents_set')
    Device_Temperature = DeviceTemperatureSerializer(many=True, read_only=True, source='devicetemperature_set')
    Power_Consumption = PowerConsumptionSerializer(many=True, read_only=True, source='power_consumption')
    Device_Configuration = DeviceConfigurationSerializer(many=True, read_only=True, source='deviceconfiguration_set')
    Performance_Metrics = PerformanceMetricsSerializer(many=True, read_only=True, source='performancemetrics_set')
    IPAddress_data = IPAddressSerializer(many=True, read_only=True, source='ipaddress_set')
    PacketLoss_Data = PacketLossDataSerializer(many=True, read_only=True, source='packetlossdata_set')
    
    class Meta:
        model = NetworkDevice
        fields = '__all__'

# class NetworkDeviceSerializer(ModelSerializer):
#     interfaces = InterfaceSerializer(many=True, read_only=True, source='interface_set')
#     Network_Events = NetworkEventsSerializer(many=True, read_only=True, source='networkevents_set')
#     Device_Temperature = DeviceTemperatureSerializer(many=True, read_only=True, source='devicetemperature_set')
#     Power_Consumption = PowerConsumptionSerializer(many=True, read_only=True, source='powerconsumption_set')  # Исправил опечатку в 'powerconsumption_set'
#     Device_Configuration = DeviceConfigurationSerializer(many=True, read_only=True, source='deviceconfiguration_set')
#     Performance_Metrics = PerformanceMetricsSerializer(many=True, read_only=True, source='performancemetrics_set')
#     # IPAddress_data = IPAddressSerializer(many=True, read_only=True, source='ip_address') # Убрано или закомментировано
#     PacketLoss_Data = PacketLossDataSerializer(many=True, read_only=True, source='packetlossdata_set')
    
#     ip_addresses = SerializerMethodField()  # Новое поле для списка IP-адресов

#     class Meta:
#         model = NetworkDevice
#         fields = '__all__'  # Исправлено на '__all__'

#     def get_ip_addresses(self, obj):
#         # Возвращает список IP-адресов как список строк
#         return [ip.ip_address for ip in obj.ip_address.all()]