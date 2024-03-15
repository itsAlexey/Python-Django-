from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from TestDB.models import NetworkDevice, User
from TestDB.serializers import NetworkDeviceSerializer, UserSerializer

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

class UsersView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UsersListView(APIView):
    """
    Возвращает список всех пользователей со всей связанной информацией.
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
