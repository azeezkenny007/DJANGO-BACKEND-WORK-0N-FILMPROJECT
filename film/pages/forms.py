# forms.py
from django.forms import ModelForm
from .models import Contact, Attendance,MyModel
from django.contrib import messages
from rest_framework.serializers import ModelSerializer


class MyModelSerializer(ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['id', 'name', 'description']



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ['course', 'student']


