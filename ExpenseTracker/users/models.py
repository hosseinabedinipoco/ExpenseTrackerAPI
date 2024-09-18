from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import check_password as check
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=300)
    username = models.CharField(max_length=150, unique=False, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def check_password(self, raw_password: str) -> bool:
        return check(raw_password, self.password)
