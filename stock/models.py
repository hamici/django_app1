from django.db import models

# Create your models here.

class Product (models.Model):
    name = models.fields.CharField(max_length=100)
    category = models.fields.CharField(max_length=25)
    price = models.fields.FloatField(default=0)
    stock_qte = models.fields.IntegerField(max_length=5,null=True)
