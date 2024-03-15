"""
URL configuration for RestApiDB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TestDB.views import NetworkDeviceListView, UsersListView

from rest_framework.routers import SimpleRouter

from TestDB.views import NetworkDeviceView, UsersView

router = SimpleRouter()

router.register('api/networkdevices', NetworkDeviceView)
router.register('api/users', UsersView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('network-devices/', NetworkDeviceListView.as_view(), name='network-device-list'),
    path('users/', UsersListView.as_view(), name='users-list'),
]

urlpatterns += router.urls