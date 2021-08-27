from .models import UserDetails
from django.contrib import admin



@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    pass
