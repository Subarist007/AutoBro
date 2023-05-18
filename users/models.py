from django.db import models
from django.contrib.auth.models import AbstractUser


"""Расширение класса пользователя"""
class User(AbstractUser):
    date_birth = models.DateField(null=True)
    car_number = models.CharField(max_length=6, null=True)
    car = models.ForeignKey(CarsBase, on_delete=models.PROTECT, null=True)

"""База данных всех автомобилей"""
class CarsBase(models.Model):
    id_mark = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    brand_rus = models.CharField(max_length=50)
    popularity = models.BooleanField(null=True)
    country = models.CharField(max_length=50)
    model_id = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    model_rus = models.CharField(max_length=50)
    auto_class = models.CharField(max_length=5)
    year_start = models.IntegerField(max_length=4)
    year_end = models.IntegerField(max_length=4)
