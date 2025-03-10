from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",
        blank=True
    )

    full_name = models.CharField(max_length=100, null = True, blank = True)
    phone = models.CharField( max_length= 11, null = True, blank = True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30, null = True, blank = True)
    address = models.CharField(max_length=150, null = True, blank = True)
    national_id = models.CharField(max_length=14, unique=True)
    birth_date = models.DateField()
    
    
    profile_image = models.ImageField(upload_to='profile_images/', null = True, blank = True)
    medical_report = models.FileField(upload_to='medical_reports/', null = True, blank = True)
    national_id_image = models.ImageField(upload_to='national_id/', null = True, blank = True)
    form_2_gond = models.FileField(upload_to='military_forms/', null = True, blank = True)
    form_6_7_gond = models.FileField(upload_to='military_forms/', null = True, blank = True)
    payment_receipt = models.FileField(upload_to='receipts/', null = True, blank = True)
    high_school_certificate = models.FileField(upload_to='certificates/', null = True, blank = True)
    final_nomination_card = models.FileField(upload_to='nomination_cards/', null = True, blank = True)
     
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['full_name', 'phone', 'national_id']

    def __str__(self):
        return self.username