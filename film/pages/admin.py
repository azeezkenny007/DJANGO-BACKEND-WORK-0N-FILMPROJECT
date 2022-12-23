from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Categorie)
admin.site.register(Film)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(User)
admin.site.register(Group)