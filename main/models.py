from distutils.command.upload import upload
from django.db import models
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Solution(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='solutions/', blank=True, null=True)
    body = RichTextField()
        
class Service(models.Model):
    body = RichTextField()


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone_number = PhoneNumberField(region='UZ')
    subject = models.CharField(max_length=500, null=True, blank=True)
    message = models.TextField()