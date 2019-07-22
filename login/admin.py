from django.contrib import admin
from .models import User, LoginLog
# Register your models here.


admin.site.site_title = "资产管理"
admin.site.site_header = "资产管理"
admin.site.index_title = "资产管理"


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'nickname', 'email', 'sex', 'status', "create_time"]


class LoginLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'event_type', 'detail', 'address', 'useragent', 'create_time']


admin.site.register(User, UserAdmin)
admin.site.register(LoginLog, LoginLogAdmin)

