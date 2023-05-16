from django.db import models
from django.contrib.auth.models import AbstractUser


"""Расширение класса пользователя"""
class User(AbstractUser):
    date_birth = models.DateField(null=True)
    car_number = models.CharField(max_length=6, null=True)
    # car = определить модель автомобиля пользователя и создать зависимость

