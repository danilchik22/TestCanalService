from django.contrib import admin
from .models import Order

@admin.register(Order)
class PersonAdmin(admin.ModelAdmin):
    pass