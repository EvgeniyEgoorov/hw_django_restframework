from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'


class Measurement(models.Model):
    temperature = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата измерения')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')

    class Meta:
        verbose_name = 'Показатель'
        verbose_name_plural = 'Показания'

