from unicodedata import category

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

#addproducts class -> addproducts table here all products are saved
class products(models.Model):
    category = models.CharField(max_length=30)
    pro_name = models.CharField(max_length=50)
    qty = models.IntegerField(max_length=10)
    mrp = models.IntegerField(max_length=10)
    discount = models.IntegerField(max_length=10)
    unit = models.CharField(max_length=20)
    date = models.DateField(max_length=50)

#cart items
class add_products(models.Model):
    pro_id = models.IntegerField(max_length=10)
    emp_id = models.IntegerField(max_length=30, default=0)
    category = models.CharField(max_length=40)
    pro_name = models.CharField(max_length=40)
    qty = models.IntegerField(max_length=40)
    mrp = models.IntegerField(max_length=10)
    unit = models.CharField(max_length=30)
    discount = models.IntegerField(max_length=30)
    amount = models.IntegerField(max_length=10)

#total sells table,
class sells_items(models.Model):
    category = models.CharField(max_length=50)
    pro_name = models.CharField(max_length=50)
    qty = models.IntegerField(max_length=20)
    mrp = models.IntegerField(max_length=20)
    unit = models.CharField(max_length=30)
    discount = models.IntegerField(max_length=20)
    amount = models.IntegerField(max_length=10)
    date = models.DateField(max_length=50)
    inv_no = models.CharField(max_length=50)
    mod = models.CharField(max_length=30, default='')

#customer table,
class customers_sells(models.Model):
    cus_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=14, null=True, blank=True)
    inv_no = models.CharField(max_length=50)
    date = models.DateField(max_length=50)
    gtotal = models.IntegerField(max_length=50)

#invoice table,
class invoice_data(models.Model):
    inv_no = models.CharField(max_length=50)
    date = models.DateField(max_length=50)
    gtotal = models.IntegerField(max_length=50)
    emp_id = models.IntegerField(max_length=50)
    emp_name = models.CharField(max_length=30)





