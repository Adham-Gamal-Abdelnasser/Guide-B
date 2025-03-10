from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields ='__all__'
        