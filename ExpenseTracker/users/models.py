from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import check_password
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=300)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def check_password(self, raw_password: str) -> bool:
        return check_password(raw_password)
