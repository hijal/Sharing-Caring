from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreation, CustomUserChange


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreation
    form = CustomUserChange
    model = CustomUser
    list_display = ['email' , 'username',  'age', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
