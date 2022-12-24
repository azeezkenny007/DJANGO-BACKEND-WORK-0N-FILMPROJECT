# forms.py
from django import forms
from .models import Contact
from django.contrib import messages


from django.db import models



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
