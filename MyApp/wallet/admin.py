from django.contrib import admin
from .models import ComboPoint
# Register your models here.

@admin.register(ComboPoint)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'image', 'price', 'point')