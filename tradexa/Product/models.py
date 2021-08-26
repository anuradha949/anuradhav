from django.db import models
from django import forms

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    price = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
   
