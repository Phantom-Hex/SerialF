from django.contrib import admin

# Register your models here.

from .models import Device, Type, Maker

admin.site.register(Device)
admin.site.register(Type)
admin.site.register(Maker)