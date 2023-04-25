from django.db import models

# Create your models here.

class Product (models.Model):
    name = models.fields.CharField(max_length=100)
    category = models.fields.CharField(max_length=25)