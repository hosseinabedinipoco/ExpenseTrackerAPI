from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ['email', 'password']
        
    def create(self, data):
        user = User.objects.create(
            email = data['email'],
            password = make_password(data['password'])
        )
        return user

        