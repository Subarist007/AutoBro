from rest_framework import serializers
from .models import User, CarsBase

class UserSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = User
        fields = "__all__"


class CarsBaseSerializer(serializers.ModelSerializer):
    pass