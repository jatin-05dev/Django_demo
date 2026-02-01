from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField()
    email=models.EmailField()
    password=models.CharField(max_length=45)
    cpassword=models.CharField(max_length=50)