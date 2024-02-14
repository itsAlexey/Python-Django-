from django.db import models

# Create your models here.

# NetworkDevice
# ├── id: Integer (PK)
# ├── name: String
# ├── device_type: String
# └── location: String


class NetworkDevice(models.Model):
    """Сетевое устройство."""
    name = models.CharField(verbose_name='Название', max_length=150)
    device_type = models.CharField(
        verbose_name='Тип устройства', max_length=50)
    location = models.CharField(verbose_name='Местонахождение', max_length=150)

    class Meta:
        verbose_name = 'Сетевое устройство'
        verbose_name_plural = 'Сетевые устройства'
        db_table = 'network_device'

    def __str__(self):
        return self.name

# Interface
# ├── id: Integer (PK)
# ├── device: ForeignKey(NetworkDevice)
# ├── name: String
# └── status: String


class Interface(models.Model):
    """Интерфейс сетевого устройства."""
    device = models.ForeignKey(
        NetworkDevice, on_delete=models.CASCADE, verbose_name='Сетевое устройство')
    name = models.CharField(verbose_name='Название интерфейса', max_length=100)
    networkBandWidth = models.FloatField(verbose_name="Пропускная способность")
    status = models.CharField(verbose_name='Статус', max_length=50)

    class Meta:
        verbose_name = 'Интерфейс'
        verbose_name_plural = 'Интерфейсы'
        db_table = 'interface'

    def __str__(self):
        return self.name

# TrafficData
# ├── id: Integer (PK)
# ├── interface: ForeignKey(Interface)
# ├── timestamp: DateTime
# ├── inbound_traffic: Float
# └── outbound_traffic: Float


class TrafficData(models.Model):
    interface = models.ForeignKey(
        Interface, on_delete=models.CASCADE, verbose_name='Интерфейс')
    timestamp = models.DateTimeField(verbose_name='Время')
    inbound_traffic = models.FloatField(verbose_name='Входящий трафик')
    outbound_traffic = models.FloatField(verbose_name='Исходящий трафик')

    class Meta:
        verbose_name = 'Данные о трафике'
        verbose_name_plural = 'Данные о трафиках'
        db_table = 'traffic_data'

    def __str__(self):
        return f"{self.interface} - {self.timestamp}"

# ErrorLog
# ├── id: Integer (PK)
# ├── device: ForeignKey(NetworkDevice)
# ├── timestamp: DateTime
# ├──  error_type: String
# └── description: Text


class ErrorLog(models.Model):
    device = models.ForeignKey(
        NetworkDevice, on_delete=models.CASCADE, verbose_name='Устройство')
    timestamp = models.DateTimeField(verbose_name='Время')
    error_type = models.CharField(max_length=100, verbose_name='Тип ошибки')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Журнал ошибок'
        verbose_name_plural = 'Журналы ошибок'
        db_table = 'error_log'

    def __str__(self):
        return f"{self.device} - {self.error_type} - {self.timestamp}"

# UserActivity
# ├── id: Integer (PK)
# ├── user_id: String
# ├── device: ForeignKey(NetworkDevice)
# ├── timestamp: DateTime
# └── activity_type: String


class UserActivity(models.Model):
    user_id = models.CharField(max_length=100, verbose_name='ID пользователя')
    device = models.ForeignKey(
        NetworkDevice, on_delete=models.CASCADE, verbose_name='Устройство')
    timestamp = models.DateTimeField(verbose_name='Время')
    activity_type = models.CharField(
        max_length=100, verbose_name='Тип активности')

    class Meta:
        verbose_name = 'Активность пользователя'
        verbose_name_plural = 'Активности пользователей'
        db_table = 'user_activity'

    def __str__(self):
        return f"{self.user_id} - {self.activity_type} - {self.timestamp}"

# BandwidthUsage
# ├── id: Integer (PK)
# ├── interface: ForeignKey(Interface)
# ├── timestamp: DateTime
# └── bandwidth_usage: Float


class BandwidthUsage(models.Model):
    interface = models.ForeignKey(
        Interface, on_delete=models.CASCADE, verbose_name='Интерфейс')
    timestamp = models.DateTimeField(verbose_name='Время')
    bandwidth_usage = models.FloatField(
        verbose_name='Использование полосы пропускания')

    class Meta:
        verbose_name = 'Использование полосы пропускания'
        verbose_name_plural = 'Использование полос пропускания'
        db_table = 'bandwidth_usage'

    def __str__(self):
        return f"{self.interface} - {self.timestamp}"

# DeviceConfiguration
# ├── id: Integer (PK)
# ├── device: ForeignKey(NetworkDevice)
# ├── configuration_timestamp: DateTime
# └── configuration_details: Text


class DeviceConfiguration(models.Model):
    device = models.ForeignKey(
        NetworkDevice, on_delete=models.CASCADE, verbose_name='Устройство')
    configuration_timestamp = models.DateTimeField(
        verbose_name='Время конфигурации')
    configuration_details = models.TextField(
        verbose_name='Детали конфигурации')

    class Meta:
        verbose_name = 'Конфигурация устройства'
        verbose_name_plural = 'Конфигурации устройств'
        db_table = 'device_configuration'

    def __str__(self):
        return f"{self.device} - {self.configuration_timestamp}"

# AuthenticationLog
# ├── id: Integer (PK)
# ├── user_id: String
# ├── device: ForeignKey(NetworkDevice)
# ├── timestamp: DateTime
# └── action_type: String


class AuthenticationLog(models.Model):
    user_id = models.CharField(max_length=100, verbose_name='ID пользователя')
    device = models.ForeignKey(
        NetworkDevice, on_delete=models.CASCADE, verbose_name='Устройство')
    timestamp = models.DateTimeField(verbose_name='Время')
    action_type = models.CharField(max_length=100, verbose_name='Тип действия')

    class Meta:
        verbose_name = 'Журнал аутентификации'
        verbose_name_plural = 'Журналы аутентификации'
        db_table = 'authentication_log'

    def __str__(self):
        return f"{self.user_id} - {self.action_type} - {self.timestamp}"

# PerformanceMetrics
# ├── id: Integer (PK)
# ├── device: ForeignKey(NetworkDevice)
# ├── timestamp: DateTime
# ├── cpu_usage: Float
# └── memory_usage: Float


class PerformanceMetrics(models.Model):
    device = models.ForeignKey(
        NetworkDevice, on_delete=models.CASCADE, verbose_name='Устройство')
    timestamp = models.DateTimeField(verbose_name='Время')
    cpu_usage = models.FloatField(verbose_name='Использование ЦПУ')
    memory_usage = models.FloatField(verbose_name='Использование памяти')

    class Meta:
        verbose_name = 'Метрики производительности'
        verbose_name_plural = 'Метрики производительности'
        db_table = 'performance_metrics'

    def __str__(self):
        return f"{self.device} - {self.timestamp}"

# NetworkEvents
# ├── id: Integer (PK)
# ├── device: ForeignKey(NetworkDevice)
# ├── event_timestamp: DateTime
# └── event_type: String
#     └── severity_level: String


class NetworkEvents(models.Model):
    device = models.ForeignKey(
        NetworkDevice, on_delete=models.CASCADE, verbose_name='Устройство')
    event_timestamp = models.DateTimeField(verbose_name='Время события')
    event_type = models.CharField(max_length=100, verbose_name='Тип события')
    severity_level = models.CharField(
        max_length=100, verbose_name='Уровень серьезности')

    class Meta:
        verbose_name = 'Сетевое событие'
        verbose_name_plural = 'Сетевые события'
        db_table = 'network_events'

    def __str__(self):
        return f"{self.device} - {self.event_type} - {self.event_timestamp}"

# IPAddress
# ├── id: Integer (PK)
# ├── device: ForeignKey(NetworkDevice)
# ├── ip_address: GenericIPAddressField
# └── is_primary: BooleanField


class IPAddress(models.Model):
    """IP-адрес сетевого устройства."""
    device = models.ForeignKey(
        NetworkDevice, on_delete=models.CASCADE, verbose_name='Сетевое устройство')
    ip_address = models.GenericIPAddressField(verbose_name='IP-адрес')
    is_primary = models.BooleanField(
        default=False, verbose_name='Основной адрес?')

    class Meta:
        verbose_name = 'IP-адрес'
        verbose_name_plural = 'IP-адреса'
        db_table = 'ip_address'

    def __str__(self):
        return self.ip_address

# Configuration
# ├── id: Integer (PK)
# ├── device: ForeignKey(NetworkDevice)
# ├── configuration_text: TextField
# └── date_added: DateTimeField


class Configuration(models.Model):
    """Конфигурация сетевого устройства."""
    device = models.ForeignKey(
        NetworkDevice, on_delete=models.CASCADE, verbose_name='Сетевое устройство')
    configuration_text = models.TextField(verbose_name='Текст конфигурации')
    date_added = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'Конфигурация'
        verbose_name_plural = 'Конфигурации'
        db_table = 'configuration'

    def __str__(self):
        return f"Конфигурация для {self.device.name} от {self.date_added.strftime('%Y-%m-%d')}"


'''class SOV(models.Model):
    """Система обнаружения вторжения."""
    device = models.ForeignKey(
        NetworkDevice, on_delete=models.CASCADE, verbose_name='Сетевое устройство')
    configuration_text = models.TextField(verbose_name='Текст конфигурации')
    date_added = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'Конфигурация'
        verbose_name_plural = 'Конфигурации'
        db_table = 'configuration'

    def __str__(self):
        return f"Конфигурация для {self.device.name} от {self.date_added.strftime('%Y-%m-%d')}"'''


# Варианты построения графиков
# 1. "Динамика трафика (входящего/исходящего) по интерфейсам за выбранный период."
# 2. "Количество ошибок на устройствах за выбранный период."
# 3. "Активность пользователей по времени суток или дням недели."
# 4. "Использование пропускной способности интерфейсов в реальном времени."
# 5. "Изменения в конфигурациях устройств."
# 6. "Логи аутентификации пользователей (успешные/неуспешные попытки)."
# 7. "Метрики производительности устройств (CPU, память)."
# 8. "Распределение типов сетевых событий по уровню серьезности."


# ### 1. График использования трафика по времени
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
