from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from TestDB.models import NetworkDevice
from TestDB.serializers import NetworkDeviceSerializer

from .models import Person
from .serializers import PersonSerializer

# Create your views here.

class NetworkDeviceView(ModelViewSet):
    queryset = NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer

class NetworkDeviceListView(APIView):
    """
    Возвращает список всех сетевых устройств со всей связанной информацией.
    """
    def get(self, request, format=None):
        devices = NetworkDevice.objects.all()
        serializer = NetworkDeviceSerializer(devices, many=True)
        return Response(serializer.data)
