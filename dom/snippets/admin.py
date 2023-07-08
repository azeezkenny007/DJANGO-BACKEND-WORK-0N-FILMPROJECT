from django.contrib import admin
from .models import Snippet,NameCategory,Attendance,Student,Todo,Room,Message

# Register your models here.
admin.site.register(Snippet)
admin.site.register(NameCategory)
admin.site.register(Attendance)
admin.site.register(Student)
admin.site.register(Todo)
admin.site.register(Room)
admin.site.register(Message)