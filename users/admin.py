from django.contrib import admin

# Register your models here.
from .models import User

admin.site.site_title = "资产管理"
admin.site.site_header = "资产管理"
admin.site.index_title = "资产管理"


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'nickname', 'password', 'email', 'first_name', "last_name"]
    
    
# admin.site.register(User, UserAdmin)

