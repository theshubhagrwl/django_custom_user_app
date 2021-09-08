from django.contrib import admin
from users.models import  CustomUser


@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ['id','email','name','password','username','session_token','active','is_staff','is_superuser','created_at','updated_at']




