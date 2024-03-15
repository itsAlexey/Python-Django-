from django.db import models

# Create your models here.

# TypeDevices
# ├── name: string
# ├── type_device: string
# ├── serial_number: string
# └── about: string

class TypeDevices(models.Model):
    """Тип устройства"""
    name = models.CharField(verbose_name='Название', max_length=150)
    type_device = models.CharField(verbose_name="Тип устройства", max_length=50)
    serial_number = models.CharField(verbose_name="Серийный номер", max_length=50)
    about = models.CharField(verbose_name="Об устройстве", max_length=200, blank=True)

    # TypeNetworkDevices = models.ForeignKey("NetworkDevice", on_delete=models.CASCADE, verbose_name="Сетевое устройство", related_name="type_network_devices")

    class Meta:
        verbose_name = 'Тип устройства'
        verbose_name_plural = 'Тип устройства'
        db_table = 'type_device'

    def __str__(self):
        return f"{self.name} / {self.type_device} / {self.serial_number}"

# HostDevice 
# ├── typeHostDevices: ForeignKey(TypeDevices)
# ├── location: String
# ├── mac_address: string
# └── active: boolean

class HostDevice(models.Model):
    """Хост-устройства"""
    location = models.CharField(verbose_name='Местонахождение', max_length=150, blank=True)
    mac_address = models.CharField(verbose_name='Mac адрес', max_length=12)
    active = models.BooleanField(default=False, verbose_name="Используется?")
    
    hostdeviceIPAddress = models.ForeignKey("IPAddress", blank=True, on_delete=models.CASCADE, verbose_name="Хост устройство")

    class Meta:
        verbose_name = 'Хост-устройства'
        verbose_name_plural = 'Хост-устройства'
        db_table = 'host_device'

    def __str__(self):
        return f"{self.typeHostDevices.type_device} / {self.typeHostDevices.name} / {self.mac_address}"

# NetworkDevice
# ├── purpose: String
# ├── location: String
# └── typeNetworkDevice: ForeignKey(TypeDevices)

class NetworkDevice(models.Model):
    """Сетевое устройство"""
    purpose = models.CharField(verbose_name='Назначение', max_length=150)
    location = models.CharField(verbose_name='Местонахождение', max_length=150, blank=True)

    typeNetworkDevice =  models.ForeignKey(TypeDevices, on_delete=models.CASCADE, null=True, verbose_name="Тип устройства", related_name="type_network_device")
    IPAddressNetworkDevice =  models.ForeignKey("IPAddress", on_delete=models.CASCADE, null=True, verbose_name="IP-адрес", related_name="ipaddress_network_device")

    class Meta:
        verbose_name = 'Сетевое устройство'
        verbose_name_plural = 'Сетевые устройства'
        db_table = 'network_device'

    def __str__(self):
        return f"{self.typeNetworkDevice.name} / {self.purpose}"

# Interface
# ├── name: String
# ├── status: String
# ├── speed: Integer (скорость интерфейса в Мбит/сек)
# ├── duplex_mode: String (режим дуплекса - полный или половинный)
# └── deviceInterface: ForeignKey(NetworkDevice)

class Interface(models.Model):
    """Интерфейс сетевого устройства"""
    name = models.CharField(verbose_name='Название интерфейса', max_length=100)
    speed = models.FloatField(verbose_name="Скорость интерфейса в Мбит/сек")
    status = models.CharField(verbose_name='Статус', max_length=50)
    duplex_mode = models.TextField(verbose_name="Режим дуплекса - полный или половинный", max_length=50)
    
    deviceInterface = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE, verbose_name="Сетевое устройство", blank=True)

    class Meta:
        verbose_name = 'Интерфейс'
        verbose_name_plural = 'Интерфейсы'
        db_table = 'interface'

    def __str__(self):
        return f"{self.name} / {self.deviceInterface.purpose}"

# TrafficData
# ├── timestamp: DateTime
# ├── inbound_traffic: Float
# ├── outbound_traffic: Float
# ├── total_packets: Float (общее количество пакетов)
# ├── error_packets: Float (количество пакетов с ошибками)
# └── interfacesTrafficData: ForeignKey(Interface)

class TrafficData(models.Model):
    """Данные о трафике"""
    timestamp = models.DateTimeField(verbose_name='Время')
    inbound_traffic = models.FloatField(verbose_name='Входящий трафик')
    outbound_traffic = models.FloatField(verbose_name='Исходящий трафик')
    time_start = models.DateTimeField(verbose_name='Время запуска')

    interfacesTrafficData = models.ForeignKey(Interface, on_delete=models.CASCADE, verbose_name="Интерфейсы")

    class Meta:
        verbose_name = 'Данные о трафике'
        verbose_name_plural = 'Данные о трафиках'
        db_table = 'traffic_data'

    def __str__(self):
        return f"{self.interfacesTrafficData.deviceInterface.typeNetworkDevice.name} / {(self.timestamp - self.time_start)} / {self.interfacesTrafficData.name} / {self.inbound_traffic} / {self.outbound_traffic}"

# BandwidthUsage
# ├── bandwidth_usage: Float
# ├── timestamp: DateTime
# └── interfacesBandwidthUsage: ForeignKey(Interface)

class BandwidthUsage(models.Model):
    """Использование полосы пропускания"""
    timestamp = models.DateTimeField(verbose_name='Время')
    bandwidth_usage = models.FloatField(verbose_name='Использование полосы пропускания')

    interfacesBandwidthUsage = models.ForeignKey(Interface, on_delete=models.CASCADE, verbose_name="Интерфейсы")

    class Meta:
        verbose_name = 'Использование полосы пропускания'
        verbose_name_plural = 'Использование полос пропускания'
        db_table = 'bandwidth_usage'

    def __str__(self):
        return f"{self.interfacesBandwidthUsage.deviceInterface.typeNetworkDevice.name} / {self.bandwidth_usage}"

# NetworkEvents
# ├── timestamp: DateTime
# ├── event_type: String
# ├── severity_level: String
# └── deviceNetworkEvents: ForeignKey(NetworkDevice)

class NetworkEvents(models.Model):
    """Сетевые события"""
    timestamp = models.DateTimeField(verbose_name='Время события')
    event_type = models.CharField(max_length=100, verbose_name='Тип события')
    severity_level = models.CharField(max_length=100, verbose_name='Уровень серьезности')

    deviceNetworkEvents = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE, verbose_name="Сетевое устройство")

    class Meta:
        verbose_name = 'Сетевое событие'
        verbose_name_plural = 'Сетевые события'
        db_table = 'network_events'

    def __str__(self):
        return f"{self.deviceNetworkEvents.typeNetworkDevice.name} / {self.event_type} / {self.severity_level}"

# DeviceTemperature
# ├── timestamp: DateTime
# ├── temperature: Float (температура устройства)
# └── deviceDeviceTemperature: ForeignKey(NetworkDevice)

class DeviceTemperature(models.Model):
    """Температура устройства"""
    timestamp = models.DateTimeField(verbose_name='Время')
    temperature = models.FloatField(verbose_name='Температура устройства')

    deviceDeviceTemperature = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE, verbose_name="Сетевое устройство")

    class Meta:
        verbose_name = 'Температура устройства'
        verbose_name_plural = 'Температура устройства'
        db_table = 'device_temperature'

    def __str__(self):
        return f"{self.deviceDeviceTemperature.typeNetworkDevice.name} / {self.temperature} / {self.timestamp.strftime('%Y-%m-%d')}"

# PowerConsumption
# ├── timestamp: DateTime
# ├── power_consumption: Float (потребление энергии)
# └── devicePowerConsumption: ForeignKey(NetworkDevice)

class PowerConsumption(models.Model):
    """Потребление энергии"""
    timestamp = models.DateTimeField(verbose_name='Время')
    power_consumption = models.FloatField(verbose_name='Потребление энергии')

    devicePowerConsumption = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE, verbose_name="Сетевое устройство", related_name="power_consumption")

    class Meta:
        verbose_name = 'Потребление энергии'
        verbose_name_plural = 'Потребление энергии'
        db_table = 'рower_сonsumption'

    def __str__(self):
        return f"{self.devicePowerConsumption.typeNetworkDevice.name} / {self.power_consumption}"

# DeviceConfiguration
# ├── timestamp: DateTime
# ├── configuration_details: Text
# └── deviceDeviceConfiguration: ForeignKey(NetworkDevice)

class DeviceConfiguration(models.Model):
    """Конфигурация устройств"""
    timestamp = models.DateTimeField(verbose_name='Время конфигурации')
    configuration_details = models.TextField(verbose_name='Детали конфигурации')

    deviceDeviceConfiguration = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE, verbose_name="Сетевое устройство")

    class Meta:
        verbose_name = 'Конфигурация устройства'
        verbose_name_plural = 'Конфигурации устройств'
        db_table = 'device_configuration'

    def __str__(self):
        return f"{self.deviceDeviceConfiguration.typeNetworkDevice.name} / {self.timestamp.strftime('%Y-%m-%d')}"

# PerformanceMetrics
# ├── timestamp: DateTime
# ├── cpu_usage: Float
# ├── memory_usage: Float
# ├── storage_usage: Float (использование хранилища)
# └── devicePerformanceMetrics: ForeignKey(NetworkDevice)

class PerformanceMetrics(models.Model):
    """Метрики производительности"""
    timestamp = models.DateTimeField(verbose_name='Время')
    cpu_usage = models.FloatField(verbose_name='Использование ЦПУ')
    memory_usage = models.FloatField(verbose_name='Использование памяти')
    storage_ussage = models.FloatField(verbose_name="Использование хранилища")

    devicePerformanceMetrics = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE, verbose_name="Сетевое устройство")

    class Meta:
        verbose_name = 'Метрики производительности'
        verbose_name_plural = 'Метрики производительности'
        db_table = 'performance_metrics'

    def __str__(self):
        return f"{self.devicePerformanceMetrics.typeNetworkDevice.name} / {self.cpu_usage} / {self.memory_usage} / {self.storage_ussage}"

# IPAddress
# ├── ip_address: GenericIPAddressField
# ├── is_primary: BooleanField
# ├── deviceIPAddress: ForeignKey(NetworkDevice)
# └── hostdeviceIPAddress: ForeignKey(HostDevice)

class IPAddress(models.Model):
    """IP-адрес сетевого устройства"""
    ip_address_device = models.GenericIPAddressField(verbose_name='IP-адрес')
    is_primary = models.BooleanField(default=False, verbose_name='Основной адрес?')

    class Meta:
        verbose_name = 'IP-адрес'
        verbose_name_plural = 'IP-адреса'
        db_table = 'ip_address'

    def __str__(self):
        return self.ip_address_device

# PacketLossData
# ├── timestamp: DateTime
# ├── packet_loss: Float (потеря пакетов)
# ├── devicePacketLossData: ForeignKey(NetworkDevice)
# └── hostdevicePacketLossData: ForeignKey(HostDevice)

class PacketLossData(models.Model):
    """Данные о потере пакетов"""
    timestamp = models.DateTimeField(verbose_name='Время')
    packet_loss = models.FloatField(verbose_name='Потеря пакетов')

    devicePacketLossData = models.ForeignKey(NetworkDevice, blank=True, on_delete=models.CASCADE, verbose_name="Сетевое устройство")
    # hostdevicePacketLossData = models.ForeignKey(HostDevice, blank=True, on_delete=models.CASCADE, verbose_name="IP адрес")

    class Meta:
        verbose_name = 'Потеря пакетов'
        verbose_name_plural = 'Потеря пакетов'
        db_table = 'packetloss_data'

    def __str__(self):
        return f"{self.packet_loss} % / {self.timestamp.strftime('%Y-%m-%d')}"

# User
# ├── user_name: String
# ├── user_lastname: String
# ├── user_surname: String
# └── user_id: String

class User(models.Model):
    """Данные пользователей"""
    user_surname = models.CharField(max_length=100, verbose_name='Фамилия')
    user_name = models.CharField(max_length=100, verbose_name='Имя')
    user_lastname = models.CharField(max_length=100, verbose_name='Отчество')
    user_id = models.CharField(max_length=100, verbose_name='ID пользователя')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'user'

    def __str__(self):
        return f"{self.user_surname} {self.user_name} / {self.user_id}"

# UserActivity
# ├── timestamp: DateTime
# ├── activity_type: String
# ├── userActivity: ForeignKey(User)
# └── deviceUserActivity: ForeignKey(NetworkDevice)

class UserActivity(models.Model):#Готово
    "Активность пользователей"
    timestamp = models.DateTimeField(verbose_name='Время')
    activity_type = models.CharField(max_length=100, verbose_name='Тип активности')

    userActivity =  models.ForeignKey(User, on_delete=models.PROTECT, null=True, verbose_name="Пользователь")
    deviceUserActivity = models.ForeignKey(NetworkDevice, blank=True, on_delete=models.CASCADE, verbose_name='Устройство')

    class Meta:
        verbose_name = 'Активность пользователя'
        verbose_name_plural = 'Активность пользователей'
        db_table = 'user_activity'

    def __str__(self):
        return f"{self.userActivity.user_surname} {self.userActivity.user_name} / {self.userActivity.user_id} / {self.activity_type} / {self.deviceUserActivity.typeNetworkDevice.name}"

# AuthenticationLog
# ├── timestamp: DateTime
# ├── action_type: String
# ├── userId: ForeignKey(Users)
# └── deviceAuthLog: ForeignKey(NetworkDevice)

class AuthenticationLog(models.Model):
    """Журналы аутентификации"""
    timestamp = models.DateTimeField(verbose_name='Время')
    action_type = models.CharField(max_length=100, verbose_name='Тип действия')

    userId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    deviceAuthLog = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE, verbose_name='Устройство')

    class Meta:
        verbose_name = 'Журнал аутентификации'
        verbose_name_plural = 'Журналы аутентификации'
        db_table = 'authentication_log'

    def __str__(self):
        return f"{self.userId.user_surname} {self.userId.user_name} / {self.action_type} {self.timestamp.strftime('%Y-%m-%d')}"


# Варианты построения графиков
# 1. "Динамика трафика (входящего/исходящего) по интерфейсам за выбранный период."
# 2. "Количество ошибок на устройствах за выбранный период."
# 3. "Активность пользователей по времени суток или дням недели."
# 4. "Использование пропускной способности интерфейсов в реальном времени."
# 5. "Изменения в конфигурациях устройств."
# 6. "Логи аутентификации пользователей (успешные/неуспешные попытки)."
# 7. "Метрики производительности устройств (CPU, память)."
# 8. "Распределение типов сетевых событий по уровню серьезности."


# ### 1. График использования трафика по network_device.last_reboot_time
# Используя данные из таблицы TrafficData, можно построить график, показывающий изменение входящего и исходящего трафика во времени для конкретного интерфейса или для всех интерфейсов сетевого устройства.
# Это поможет определить пики активности и возможные проблемы с пропускной способностью.

# ### 2. График ошибок устройств
# Из таблицы ErrorLog можно извлечь данные о количестве ошибок, зарегистрированных на различных устройствах, и отобразить их на графике по времени.
# Это даст представление о стабильности работы устройств и поможет выявить устройства с повышенным уровнем ошибок.

# ### 3. Анализ активности пользователей
# Данные из таблицы UserActivity могут быть использованы для создания графика, отображающего активность пользователей за определенный период.
# Это может включать количество активных сессий, типы выполняемых операций и т.д. Такой анализ может помочь в выявлении аномальной активности или планировании ресурсов.

# ### 4. Мониторинг использования полосы пропускания
# С помощью данных из таблицы BandwidthUsage можно визуализировать использование полосы пропускания интерфейсами сетевых устройств.
# График может показать, как меняется загрузка канала во времени, что поможет выявить моменты перегрузки и спланировать расширение инфраструктуры.

# ### 5. Изменения конфигурации устройств
# Из таблицы DeviceConfiguration можно получить информацию об изменениях конфигураций устройств.
# Визуализация этих данных поможет отслеживать частоту и объем изменений, а также выявить корреляцию между изменениями конфигурации и возникающими проблемами.

# ### 6. Журнал аутентификации
# Данные из AuthenticationLog могут быть использованы для создания графика, отображающего количество успешных и неудачных попыток аутентификации по времени или пользователям.
# Это поможет выявить подозрительную активность или проблемы с доступом.

# ### Инструменты для построения графиков
# Для построения графиков можно использовать различные инструменты и библиотеки, такие как Matplotlib и Seaborn в Python, или интегрированные решения для веб-приложений, например, D3.js или Chart.js.
# Выбор инструмента зависит от требований к визуализации и платформы, на которой реализовано приложение.
##############################################################################
# ### 2. Проверка сериализатора

# Проблема может заключаться в вашем сериализаторе NetworkDeviceSerializer. Убедитесь, что он правильно настроен для работы с множественными объектами.

# - В вашем сериализаторе должен быть корректно настроен Meta класс, а также должны быть правильно определены поля, которые вы хотите сериализовать.
# - Если у вас есть вложенные сериализаторы (например, для интерфейсов), убедитесь, что они также корректно обрабатывают множественные объекты.

# ### 3. Проверка запроса к базе данных

# Возможно, запрос к базе данных не формируется так, как вы ожидаете. Django ORM очень мощный инструмент, но иногда может быть не совсем очевидно, как он работает под капотом.

# - Используйте print(devices.query) перед сериализацией объектов, чтобы увидеть сформированный SQL-запрос. Это поможет понять, какие данные извлекаются из базы.
# - Убедитесь, что нет дополнительных фильтров или аннотаций, которые могут изменять результат запроса.

# ### 4. Проверка наличия данных для сериализации

# Убедитесь, что у всех ожидаемых объектов есть данные, которые могут быть сериализованы. Если какие-то данные отсутствуют или не соответствуют ожиданиям сериализатора, это может привести к тому, что некоторые объекты будут пропущены.

# ### Решение

# Если после проверки вышеуказанных пунктов проблема остаётся, попробуйте упростить запрос до минимума и постепенно добавлять сложность (например, начните с сериализации только основных полей модели NetworkDevice, без вложенных объектов). Это поможет локализовать проблему.

# Также может помочь использование Django shell (python manage.py shell) для выполнения запросов к базе данных и сериализации в интерактивном режиме. Это позволит вам экспериментировать с различными запросами и настройками сериализатора в более контролируемой среде.

# Если проблема всё ещё не решена, предоставьте более подробную информацию о вашем сериализаторе NetworkDeviceSerializer и структуре связанных моделей. Это поможет дать более точные рекомендации.


