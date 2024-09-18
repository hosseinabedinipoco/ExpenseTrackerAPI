from django.db import models
from users.models import User

# Create your models here.
class Expense(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    category = models.CharField(max_length=20)