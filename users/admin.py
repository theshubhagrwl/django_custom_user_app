from django.contrib import admin
from .models import CustomUser
# Register your models here.

# admin.site.register(CustomUser)
@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ['id','email','name','username','session_token','active','is_staff','is_superuser','created_at','updated_at']



