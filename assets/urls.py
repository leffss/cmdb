
from django.urls import path
from . import views


app_name = 'assets'
urlpatterns = [
    path('', views.index, name='index'),
    path('hardware/', views.hardware_assets, name='hardware'),
    path('hardware/del/', views.delete_hardware_assets, name='hardware_delete'),
    path('hardware/add/', views.add_hardware_assets, name='hardware_add'),
    path('software/', views.software_assets, name='software'),
    path('software/del/', views.delete_software_assets, name='software_delete'),
    path('software/add/', views.add_software_assets, name='software_add'),
    path('detail/<int:asset_id>/', views.detail, name='detail'),
    path('audit/operation/', views.operation, name='operation'),
    path('audit/login/', views.audit_login, name='audit_login'),
]

