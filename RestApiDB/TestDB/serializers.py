from rest_framework.serializers import ModelSerializer

from .models import NetworkDevice


class NetworkDeviceSerializer(ModelSerializer):
    class Meta:
        model = NetworkDevice
        fields = '__all__'