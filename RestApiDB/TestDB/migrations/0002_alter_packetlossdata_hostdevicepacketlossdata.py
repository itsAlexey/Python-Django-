# Generated by Django 4.2.9 on 2024-03-14 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TestDB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packetlossdata',
            name='hostdevicePacketLossData',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='TestDB.hostdevice', verbose_name='IP адрес'),
        ),
    ]