from django.contrib import admin
from .models import Car, SparePart, Shop


# Register your models here.

admin.site.register(Car)
admin.site.register(SparePart)
admin.site.register(Shop)
