from django.contrib import admin
from .models import Car
@admin.register(Car)
class ArabaAdmin(admin.ModelAdmin):
    list_display = ('Model', 'Ulke')