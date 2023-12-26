# serializers.py
from rest_framework import serializers
from myAuth.models import Person
from .models import RegistrationUser
class RegistrationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationUser
        fields = ['mail', 'password', 'confirmPassword']
class PersonGet(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['mail', 'password']
