from django.contrib import admin
from .models import Snippet,NameCategory,Attendance,Student

# Register your models here.
admin.site.register(Snippet)
admin.site.register(NameCategory)
admin.site.register(Attendance)
admin.site.register(Student)
