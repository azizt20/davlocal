from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget
from django import forms
from django.forms import TextInput, EmailInput
from django.forms import ModelForm
from main.models import *



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'w-full form-input px-4 py-4 rounded-xl text-lg mt-[14px] bg-white-grey border-0 placeholder:text'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'class': 'w-full form-input px-4 py-4 rounded-xl text-lg mt-[14px] bg-white-grey border-0 placeholder:text'}),
            'phone_number': RegionalPhoneNumberWidget(attrs={'placeholder': 'Phone Number', 'class': 'w-full form-input px-4 py-4 rounded-xl text-lg mt-[14px] bg-white-grey border-0 placeholder:text'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'w-full form-input px-4 py-4 rounded-xl text-lg mt-[14px] bg-white-grey border-0 placeholder:text'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message', 'class': 'w-full  px-4 py-4 rounded-xl text-lg mt-[14px] bg-white-grey border-0 placeholder:text', 'rows': "4"}),
      
       }

