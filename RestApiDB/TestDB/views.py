from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from TestDB.models import NetworkDevice
from TestDB.serializers import NetworkDeviceSerializer

# Create your views here.

class NetworkDeviceView(ModelViewSet):
    queryset = NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer