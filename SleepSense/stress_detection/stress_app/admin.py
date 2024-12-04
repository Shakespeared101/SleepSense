from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserInputs

admin.site.register(UserInputs)  # Register UserInputs model for admin panel
