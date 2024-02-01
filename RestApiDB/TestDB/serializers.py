from rest_framework.serializers import ModelSerializer

from .models import NetworkDevice, Interface, TrafficData, ErrorLog, UserActivity, BandwidthUsage, DeviceConfiguration
from .models import AuthenticationLog, PerformanceMetrics, NetworkEvents, IPAddress, Configuration

class ErrorLogSerializer(ModelSerializer):
    class Meta:
        model = ErrorLog
        fields = '__all__'

class UserActivitySerializer(ModelSerializer):
    class Meta:
        model = UserActivity
        fields = '__all__'

class BandwidthUsageSerializer(ModelSerializer):
    class Meta:
        model = BandwidthUsage
        fields = '__all__'

class DeviceConfigurationSerializer(ModelSerializer):
    class Meta:
        model = DeviceConfiguration
        fields = '__all__'

class AuthenticationLogSerializer(ModelSerializer):
    class Meta:
        model = AuthenticationLog
        fields = '__all__'

class PerformanceMetricsSerializer(ModelSerializer):
    class Meta:
        model = PerformanceMetrics
        fields = '__all__'

class TrafficDataSerializer(ModelSerializer):
    class Meta:
        model = TrafficData
        fields = '__all__'

class NetworkEventsSerializer(ModelSerializer):
    class Meta:
        model = NetworkEvents
        fields = '__all__'

class IPAddressSerializer(ModelSerializer):
    class Meta:
        model = IPAddress
        fields = '__all__'

class ConfigurationSerializer(ModelSerializer):
    class Meta:
        model = Configuration
        fields = '__all__'

class InterfaceSerializer(ModelSerializer):
    traffic_data = TrafficDataSerializer(many=True, read_only=True)
    bandwidth_usage = BandwidthUsageSerializer(many=True, read_only=True)

    class Meta:
        model = Interface
        fields = ['id', 'name', 'status', 'traffic_data', 'bandwidth_usage']

class NetworkDeviceSerializer(ModelSerializer):
    interfaces = InterfaceSerializer(many=True, read_only=True, source='interface_set')
    error_logs = ErrorLogSerializer(many=True, read_only=True)
    user_activities = UserActivitySerializer(many=True, read_only=True)
    device_configurations = DeviceConfigurationSerializer(many=True, read_only=True)

    class Meta:
        model = NetworkDevice
        fields = ['id', 'name', 'device_type', 'location', 'interfaces', 'error_logs', 'user_activities', 'device_configurations']