from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Vendor(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email



class Shop_detail(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Vendor,on_delete=models.CASCADE,related_name="shops")
    type_of_business = models.CharField(max_length=100)
    latitude=models.FloatField()
    longitude = models.FloatField()
    def __str__(self):
        return self.name

