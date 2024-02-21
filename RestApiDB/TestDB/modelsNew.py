from django.db import models

class NetworkDevice(models.Model):
    """Сетевое устройство."""
    name = models.CharField(verbose_name='Название', max_length=150)
    device_type = models.CharField(verbose_name='Тип устройства', max_length=50)
    location = models.CharField(verbose_name='Местонахождение', max_length=150)
    
    interfaceND = models.ForeignKey('Interface', on_delete=models.PROTECT, null=True)
    typeNetDevicesND = models.ForeignKey('TypeDevices', on_delete=models.PROTECT, null=True)
    ErrorLogND = models.ForeignKey('ErrorLog', on_delete=models.PROTECT, null=True)
    
    class Meta:
        verbose_name = 'Сетевое устройство'
        verbose_name_plural = 'Сетевые устройства'
        db_table = 'network_device'

    def __str__(self):
        return f"{self.type} / {self.name}"

class Interface(models.Model):
    """Интерфейс сетевого устройства."""
    name = models.CharField(verbose_name='Название интерфейса', max_length=100)
    speed = models.FloatField(verbose_name="Скорость интерфейса в Мбит/сек")
    status = models.CharField(verbose_name='Статус', max_length=50)
    duplex_mode = models.TextField(verbose_name="Режим дуплекса - полный или половинный", max_length=50)

    trafficDataInterface = models.ForeignKey('traffic_data', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Интерфейс'
        verbose_name_plural = 'Интерфейсы'
        db_table = 'interface'

    def __str__(self):
        return self.name

class TypeDevices(models.Model):
    type = models.CharField(verbose_name="Тип устройства", max_length=50)
    serial_number = models.CharField(verbose_name="Серийный номер", max_length=50)
    about = models.CharField(verbose_name="Об устройстве", max_length=200, blank=True)
    
    class Meta:
        verbose_name = 'Тип устройства'
        verbose_name_plural = 'Тип устройства'
        db_table = 'typedevice'

    def __str__(self):
        return f"{self.type} / {self.serial_number}"

class TrafficData(models.Model):
    # interface = models.ForeignKey(Interface, on_delete=models.CASCADE, verbose_name='Интерфейс')
    timestamp = models.DateTimeField(verbose_name='Время')
    inbound_traffic = models.FloatField(verbose_name='Входящий трафик')
    outbound_traffic = models.FloatField(verbose_name='Исходящий трафик')
    total_packets = models.FloatField(verbose_name="Общее количество пакетов")
    error_packets = models.FloatField(verbose_name="Количество пакетов с ошибками")

    class Meta:
        verbose_name = 'Данные о трафике'
        verbose_name_plural = 'Данные о трафиках'
        db_table = 'traffic_data'

    def __str__(self):
        return f"{self.interface} - {self.timestamp}"

class ErrorLog(models.Model):
    timestamp = models.DateTimeField(verbose_name='Время')
    error_type = models.CharField(max_length=100, verbose_name='Тип ошибки')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Журнал ошибок'
        verbose_name_plural = 'Журналы ошибок'
        db_table = 'error_log'

    def __str__(self):
        return f"{self.device} - {self.error_type} - {self.timestamp}"
