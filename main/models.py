from django.db import models
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.


class Solution(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('title'), max_length=200),
        image = models.FileField(_('image'), upload_to='solutions/',  blank=True, null=True),
        body = RichTextField(_('body'))
    )
        
class Service(TranslatableModel):
    translations = TranslatedFields(
        body = RichTextField(_('body'))
    )


class Contact(models.Model):
    name = models.CharField(_('name'), max_length=200)
    email = models.EmailField(_('email'), blank=True, null=True)
    phone_number = PhoneNumberField(_('phone_number'), region='UZ')
    subject = models.CharField(_('subject'), max_length=500, null=True, blank=True)
    message = models.TextField(_('message'))