from django.contrib import admin
from .models import Asset, Server, SecurityDevice, StorageDevice, NetworkDevice, Software, IDC, Manufacturer
from .models import BusinessUnit, Contract, Tag, CPU, RAM, Disk, NIC, EventLog, NewAssetApprovalZone
# Register your models here.


admin.site.site_title = "资产管理"
admin.site.site_header = "资产管理"
admin.site.index_title = "资产管理"


class AssetAdmin(admin.ModelAdmin):
    list_display = ['asset_type', 'name', 'status', 'approved_by', 'c_time', "m_time"]


class NewAssetAdmin(admin.ModelAdmin):
    list_display = ['asset_type', 'sn', 'model', 'manufacturer', 'c_time', 'm_time']
    list_filter = ['asset_type', 'manufacturer', 'c_time']
    search_fields = ('sn',)


admin.site.register(Asset, AssetAdmin)
admin.site.register(Server)
admin.site.register(SecurityDevice)
admin.site.register(StorageDevice)
admin.site.register(NetworkDevice)
admin.site.register(Software)
admin.site.register(IDC)
admin.site.register(Manufacturer)
admin.site.register(BusinessUnit)
admin.site.register(Contract)
admin.site.register(Tag)
admin.site.register(CPU)
admin.site.register(RAM)
admin.site.register(Disk)
admin.site.register(NIC)
admin.site.register(EventLog)
admin.site.register(NewAssetApprovalZone, NewAssetAdmin)

