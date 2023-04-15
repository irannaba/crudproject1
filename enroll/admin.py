from django.contrib import admin
from .models import Usertable
# Register your models here.
@admin.register(Usertable)
class UserAdmin(admin.ModelAdmin):
 list_display = ('id', 'name', 'email', 'password')
