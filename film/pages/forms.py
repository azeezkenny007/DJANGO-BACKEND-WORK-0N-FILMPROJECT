# forms.py
from django.forms import ModelForm
from .models import Contact
from django.contrib import messages


from django.db import models



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
