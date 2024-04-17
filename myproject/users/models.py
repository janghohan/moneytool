from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customer(models.Model):
    customerIx = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    pwd = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
