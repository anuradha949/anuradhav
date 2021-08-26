from django.db import models
from django import forms
from django.forms import widgets

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)#widgets=forms.PasswordInput
    username = models.CharField(max_length=200)
   

class Post(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    text = models.CharField(max_length=200)#widgets=forms.Textarea
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
   