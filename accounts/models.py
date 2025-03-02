from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    full_name_ar=models.CharField(max_length=50,verbose_name='full name Arabic')
    full_name_en=models.CharField(max_length=50,verbose_name='full name English')
    national_id=models.CharField(max_length=14,unique=True,verbose_name='National ID')
    def __str__(self):
            return self.username 