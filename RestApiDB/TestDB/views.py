from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from TestDB.models import NetworkDevice, TypeDevices
from TestDB.serializers import NetworkDeviceSerializer, TypeDevicesSerializer

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
    def post(self, request, format=None):
        serializer = NetworkDeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
