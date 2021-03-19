from django.contrib import admin
from .models import polls,choice
# Register your models here.

admin.site.register(polls)
admin.site.register(choice)
