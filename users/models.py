from django.db import models
from django.contrib.auth.models import AbstractUser


"""Расширение класса пользователя"""
class User(AbstractUser):
    date_birth = models.DateField(null=True, blank=True)
    car_number = models.CharField(max_length=6, null=True, blank=True)
    car = models.ForeignKey('CarsBase', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f'{self.username}   {self.car}'

"""База данных всех автомобилей"""
class CarsBase(models.Model):
    id_mark = models.CharField(max_length=50, null=True)
    brand = models.CharField(max_length=50, null=True)
    brand_rus = models.CharField(max_length=50, null=True)
    popularity = models.BooleanField(null=True)
    country = models.CharField(max_length=50, null=True)
    model_id = models.CharField(max_length=50, null=True)
    model = models.CharField(max_length=50, null=True)
    model_rus = models.CharField(max_length=50, null=True)
    auto_class = models.CharField(max_length=5, null=True)
    year_start = models.IntegerField(null=True)
    year_end = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.brand}, {self.model}'
