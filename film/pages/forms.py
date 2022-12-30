# forms.py
from django.forms import ModelForm
from .models import Contact, Attendance
from django.contrib import messages


from django.db import models


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ['course', 'student']
