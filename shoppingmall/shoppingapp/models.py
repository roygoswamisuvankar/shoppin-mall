from django.db import models

# Create your models here.

#admin class -> admin table
class admin2(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

#employee class -> employee table
class employee2(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    dept = models.CharField(max_length=10)
    password = models.CharField(max_length=100)