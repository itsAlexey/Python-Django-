from django.db import models

# Create your models here.

# TypeDevices
# ├── type: string
# ├── serial_number: string
# └── about: string

class TypeDevices(models.Model):
    """Тип устройства"""
    name = models.CharField(verbose_name='Название', max_length=150)
    typeDevice = models.CharField(verbose_name="Тип устройства", max_length=50)
    serial_number = models.CharField(verbose_name="Серийный номер", max_length=50)
    about = models.CharField(verbose_name="Об устройстве", max_length=200, blank=True)
    
    # device = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE, verbose_name='Сетевое устройство')
    # hostDev = models.ForeignKey("HostDevice", on_delete=models.CASCADE, verbose_name='Хост устройство')
    
    class Meta:
        verbose_name = 'Тип устройства'
        verbose_name_plural = 'Тип устройства'
        db_table = 'typedevice'

    def __str__(self):
        return f"{self.name} / {self.serial_number}"

# HostDevice 
# ├── id: Integer (PK)
# ├── typeNetDevicesHost: ForeignKey(TypeDevices)
# ├── location: String
# ├── IPAddressHost: ForeignKey(IPAddress)
# ├── packetLossHost: ForeignKey(PacketLossData)
# ├── mac_address: string
# └── active: boolean

class HostDevice(models.Model):
    """Хост-устройства"""
    location = models.CharField(verbose_name='Местонахождение', max_length=150)
    mac_address = models.CharField(verbose_name='Mac адрес', max_length=12)
    active = models.BooleanField(default=False, verbose_name="Используется?")
    
    typeHostDevices =  models.ForeignKey(TypeDevices, on_delete=models.CASCADE, null=True, verbose_name="Тип устройства")
    # ipAddresshost =  models.ForeignKey('IPAdress', on_delete=models.CASCADE, null=True, verbose_name="IP адрес")
    # packetLossHost =  models.ForeignKey('PacketLossData', on_delete=models.CASCADE, null=True, verbose_name="Потеря пакетов")
    
    class Meta:
        verbose_name = 'Хост-устройства'
        verbose_name_plural = 'Хост-устройства'
        db_table = 'hostdevice'

    def __str__(self):
        return f"{self.typeHostDevices.typeDevice} {self.typeHostDevices.name}"

# NetworkDevice
# ├── id: Integer (PK)
# ├── name: String
# ├── device_type: String
# ├── location: String
# ├── interfaceND: ForeignKey(Interface)
# ├── typeNetDevicesND: ForeignKey(TypeDevices)
# ├── networkDeviceTemperature: ForeignKey(NetworkDeviceTemperature)
# ├── DeviceConfiguration: ForeignKey(DeviceConfiguration)
# ├── PerformanceMetrics: ForeignKey(PerformanceMetrics)

# ├── networkEventsInterface: ForeignKey(NetworkEvents)
# └── ErrorLogND: ForeignKey(ErrorLog)

class NetworkDevice(models.Model):
    """Сетевое устройство."""
    device_type = models.CharField(verbose_name='Тип устройства', max_length=50)
    location = models.CharField(verbose_name='Местонахождение', max_length=150)

    typeNetworkDevice =  models.ForeignKey(TypeDevices, on_delete=models.CASCADE, null=True, verbose_name="Тип устройства")
    
    # interfaceND = models.ForeignKey('Interface', on_delete=models.PROTECT, null=True, verbose_name="Интерфейс")
    # typeNetDevicesND = models.ForeignKey('TypeDevices', on_delete=models.PROTECT, null=True, verbose_name="Тип сетевого устройства")
    # networkEventsInterface = models.ForeignKey('NetworkEvents', on_delete=models.PROTECT, null=True, verbose_name="Сетевые события")
    # networkDeviceTemperature = models.ForeignKey('NetworkDeviceTemperature', on_delete=models.PROTECTED, null=True, verbose_name="Температура устрйоства")
    # PowerConsumption = models.ForeignKey('PowerConsumption', on_delete=models.PROTECTED, null=True, verbose_name="Потребление энергии")
    # DeviceConfiguration= models.ForeignKey('DeviceConfiguration', on_delete=models.PROTECTED, null=True, verbose_name="Конфигурация устройств")
    # PerformanceMetrics= models.ForeignKey('PerformanceMetrics', on_delete=models.PROTECTED, null=True, verbose_name="Метрики производительности")
    # networkIPAddress= models.ForeignKey('IPAddress', on_delete=models.PROTECTED, null=True, verbose_name="IP адрес")
    # networkPacketLossData= models.ForeignKey('PacketLossData', on_delete=models.PROTECTED, null=True, verbose_name="Потери пакетов")
    
    class Meta:
        verbose_name = 'Сетевое устройство'
        verbose_name_plural = 'Сетевые устройства'
        db_table = 'network_device'

    def __str__(self):
        return f"{self.device_type}"

# Interface
# ├── id: Integer (PK)
# ├── device: ForeignKey(NetworkDevice)
# ├── name: String
# ├── status: String
# ├── speed: Integer (скорость интерфейса в Мбит/сек)
# ├── trafficDataInterface: ForeignKey(TrafficData)
# ├── trafficDataInterface: ForeignKey(BandwidthUsage)
# └── duplex_mode: String (режим дуплекса - полный или половинный)

class Interface(models.Model):
    """Интерфейс сетевого устройства."""
    name = models.CharField(verbose_name='Название интерфейса', max_length=100)
    speed = models.FloatField(verbose_name="Скорость интерфейса в Мбит/сек")
    status = models.CharField(verbose_name='Статус', max_length=50)
    duplex_mode = models.TextField(verbose_name="Режим дуплекса - полный или половинный", max_length=50)
    
    device_interface = models.ForeignKey(NetworkDevice, blank=True, on_delete=models.CASCADE, verbose_name="Сетевое устройство")

    # trafficDataInterface = models.ForeignKey('TrafficData', on_delete=models.PROTECT, null=True, verbose_name="Данные о трафике")
    # bandwidthUsageInterface = models.ForeignKey('BandwidthUsage', on_delete=models.PROTECT, null=True, verbose_name="Использование полосы пропускания")

    class Meta:
        verbose_name = 'Интерфейс'
        verbose_name_plural = 'Интерфейсы'
        db_table = 'interface'

    def __str__(self):
        return self.name

# TrafficData
# ├── id: Integer (PK)
# ├── timestamp: DateTime
# ├── inbound_traffic: Float
# ├── outbound_traffic: Float
# ├── total_packets: Integer (общее количество пакетов)
# └── error_packets: Integer (количество пакетов с ошибками)

class TrafficData(models.Model):
    """Данные о трафике"""
    timestamp = models.DateTimeField(verbose_name='Время')
    inbound_traffic = models.FloatField(verbose_name='Входящий трафик')
    outbound_traffic = models.FloatField(verbose_name='Исходящий трафик')
    total_packets = models.FloatField(verbose_name="Общее количество пакетов")
    error_packets = models.FloatField(verbose_name="Количество пакетов с ошибками")

    interfaces_trafficData = models.ForeignKey(Interface, on_delete=models.CASCADE, verbose_name="Интерфейсы")

    class Meta:
        verbose_name = 'Данные о трафике'
        verbose_name_plural = 'Данные о трафиках'
        db_table = 'traffic_data'

    def __str__(self):
        return f"{self.interface} - {self.timestamp}"

# BandwidthUsage
# ├── id: Integer (PK)
# ├── timestamp: DateTime
# └── bandwidth_usage: Float

class BandwidthUsage(models.Model):
    """Использование полосы пропускания"""
    timestamp = models.DateTimeField(verbose_name='Время')
    bandwidth_usage = models.FloatField(verbose_name='Использование полосы пропускания')

    interfaces_bandwidthUsage = models.ForeignKey(Interface, on_delete=models.CASCADE, verbose_name="Интерфейсы")

    class Meta:
        verbose_name = 'Использование полосы пропускания'
        verbose_name_plural = 'Использование полос пропускания'
        db_table = 'bandwidth_usage'

    def __str__(self):
        return f"{self.interface} - {self.timestamp}"

# NetworkEvents
# ├── id: Integer (PK)
# ├── event_timestamp: DateTime
# ├── event_type: String
# └── severity_level: String

class NetworkEvents(models.Model):
    """Сетевые события"""
    event_timestamp = models.DateTimeField(verbose_name='Время события')
    event_type = models.CharField(max_length=100, verbose_name='Тип события')
    severity_level = models.CharField(max_length=100, verbose_name='Уровень серьезности')

    device_networkEvents = models.ForeignKey(NetworkDevice, blank=True, on_delete=models.CASCADE, verbose_name="Сетевое устройство")

    class Meta:
        verbose_name = 'Сетевое событие'
        verbose_name_plural = 'Сетевые события'
        db_table = 'network_events'

    def __str__(self):
        return f"{self.device} - {self.event_type} - {self.event_timestamp}"

# DeviceTemperature
# ├── id: Integer (PK)
# ├── timestamp: DateTime
# └── temperature: Float (температура устройства)

class DeviceTemperature(models.Model):
    """Температура устройства."""
    timestamp = models.DateTimeField(verbose_name='Время')
    temperature = models.FloatField(verbose_name='Температура устройства')

    device_deviceTemperature = models.ForeignKey(NetworkDevice, blank=True, on_delete=models.CASCADE, verbose_name="Сетевое устройство")

    class Meta:
        verbose_name = 'Температура устройства'
        verbose_name_plural = 'Температура устройства'
        db_table = 'device_temperature'

    def __str__(self):
        return f"Температура {self.temperature} {self.timestamp.strftime('%Y-%m-%d')}"

# PowerConsumption
# ├── id: Integer (PK)
# ├── timestamp: DateTime
# └── power_consumption: Float (потребление энергии)

class PowerConsumption(models.Model):
    """Потребление энергии."""
    timestamp = models.DateTimeField(verbose_name='Время')
    power_consumption = models.FloatField(verbose_name='Потребление энергии')

    device_powerConsumption = models.ForeignKey(NetworkDevice, blank=True, on_delete=models.CASCADE, verbose_name="Сетевое устройство")

    class Meta:
        verbose_name = 'Потребление энергии'
        verbose_name_plural = 'Потребление энергии'
        db_table = 'рower_сonsumption'

    def __str__(self):
        return f"Расход энергии {self.power_consumption} {self.timestamp.strftime('%Y-%m-%d')}"

# DeviceConfiguration
# ├── id: Integer (PK)
# ├── configuration_timestamp: DateTime
# └── configuration_details: Text

class DeviceConfiguration(models.Model):
    """Конфигурация устройств"""
    configuration_timestamp = models.DateTimeField(verbose_name='Время конфигурации')
    configuration_details = models.TextField(verbose_name='Детали конфигурации')

    device_deviceConfiguration = models.ForeignKey(NetworkDevice, blank=True, on_delete=models.CASCADE, verbose_name="Сетевое устройство")

    class Meta:
        verbose_name = 'Конфигурация устройства'
        verbose_name_plural = 'Конфигурации устройств'
        db_table = 'device_configuration'

    def __str__(self):
        return f"{self.device} - {self.configuration_timestamp}"

# PerformanceMetrics
# ├── id: Integer (PK)
# ├── timestamp: DateTime
# ├── cpu_usage: Float
# ├── memory_usage: Float
# └── storage_usage: Float (использование хранилища)

class PerformanceMetrics(models.Model):
    """Метрики производительности"""
    timestamp = models.DateTimeField(verbose_name='Время')
    cpu_usage = models.FloatField(verbose_name='Использование ЦПУ')
    memory_usage = models.FloatField(verbose_name='Использование памяти')
    storage_ussage = models.FloatField(verbose_name="Использование хранилища")

    device_performanceMetrics = models.ForeignKey(NetworkDevice, blank=True, on_delete=models.CASCADE, verbose_name="Сетевое устройство")

    class Meta:
        verbose_name = 'Метрики производительности'
        verbose_name_plural = 'Метрики производительности'
        db_table = 'performance_metrics'

    def __str__(self):
        return f"{self.device} - {self.timestamp}"

# IPAddress
# ├── id: Integer (PK)
# ├── ip_address: GenericIPAddressField
# └── is_primary: BooleanField

class IPAddress(models.Model):
    """IP-адрес сетевого устройства."""
    ip_address = models.GenericIPAddressField(verbose_name='IP-адрес')
    is_primary = models.BooleanField(default=False, verbose_name='Основной адрес?')

    device_IPAddress = models.ForeignKey(NetworkDevice, blank=True, on_delete=models.CASCADE, verbose_name="Сетевое устройство")
    hostdevice_IPAddress = models.ForeignKey(HostDevice, on_delete=models.CASCADE, verbose_name="Хост устройство")

    class Meta:
        verbose_name = 'IP-адрес'
        verbose_name_plural = 'IP-адреса'
        db_table = 'ip_address'

    def __str__(self):
        return self.ip_address

# PacketLossData
# ├── hostaName_loss: ForeignKey(NetworkDevice)
# ├── timestamp: DateTime
# ├── packet_loss: ForeignKey(HostDevice)
# └── packet_loss: Float (потеря пакетов)

class PacketLossData(models.Model):
    """Данные о потере пакетов."""
    timestamp = models.DateTimeField(verbose_name='Время')
    packet_loss = models.FloatField(verbose_name='Потеря пакетов')

    device_packetLossData = models.ForeignKey(NetworkDevice, blank=True, on_delete=models.CASCADE, verbose_name="Сетевое устройство")
    hostdevice_packetLossData = models.ForeignKey(HostDevice, on_delete=models.CASCADE, verbose_name="Хост устройство")

    class Meta:
        verbose_name = 'Потеря пакетов'
        verbose_name_plural = 'Потеря пакетов'
        db_table = 'packetloss_data'

    def __str__(self):
        return f"Потеря пакетов {self.packet_loss} {self.timestamp.strftime('%Y-%m-%d')}"

# User
# ├── user_name: String
# ├── user_lastname: String
# ├── user_surname: String
# └── user_id: String

class User(models.Model):
    """Данные пользователей"""
    user_surname = models.CharField(max_length=100, verbose_name='Фамилия')
    user_name = models.CharField(max_length=100, verbose_name='Имя')
    user_lastname = models.CharField(max_length=100, verbose_name='Отчество ')
    user_id = models.CharField(max_length=100, verbose_name='ID пользователя')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'user'

    def __str__(self):
        return f"{self.user_surname} - {self.user_name} / {self.user_id}"

# UserActivity
# ├── device: ForeignKey(NetworkDevice)
# ├── username: ForeignKey(User)
# ├── timestamp: DateTime
# └── activity_type: String

class UserActivity(models.Model):
    timestamp = models.DateTimeField(verbose_name='Время')
    activity_type = models.CharField(max_length=100, verbose_name='Тип активности')

    user_activity =  models.ForeignKey(User, on_delete=models.PROTECT, null=True, verbose_name="Пользователь")
    device_userActivity = models.ForeignKey(NetworkDevice, blank=True, on_delete=models.CASCADE, verbose_name='Устройство')

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
        db_table = 'user'

    def __str__(self):
        return f"{self.user_surname} - {self.user_name} - {self.user_id}"

# AuthenticationLog
# ├── user_id: ForeignKey(Users)
# ├── device: ForeignKey(NetworkDevice)
# ├── timestamp: DateTime
# └── action_type: String

class AuthenticationLog(models.Model):
    """Журналы аутентификации"""
    timestamp = models.DateTimeField(verbose_name='Время')
    action_type = models.CharField(max_length=100, verbose_name='Тип действия')

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    device = models.ForeignKey(NetworkDevice, blank=True, on_delete=models.CASCADE, verbose_name='Устройство')

    class Meta:
        verbose_name = 'Журнал аутентификации'
        verbose_name_plural = 'Журналы аутентификации'
        db_table = 'authentication_log'

    def __str__(self):
        return f"{self.user_id} {self.action_type} {self.timestamp}"


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


