from django.urls import path
from . import views


app_name = 'login'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('changepasswd/', views.change_passwd, name='changepasswd'),
    path('userinfo/', views.user_info, name='userinfo'),
]

