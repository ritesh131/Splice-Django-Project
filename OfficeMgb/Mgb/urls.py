"""OfficeMgb URL Configuration
"""
from django.contrib import admin
from django.urls import path
from knox import views as knox_views
from rest_framework.authtoken.views import obtain_auth_token

# Import views for handle request
from .views import (
    home_view, User_Register, UserLogin, 
    UserLogOut, RegisterAPI, LoginAPI
)

urlpatterns = [
    path('', home_view, name='home'),
    path('login', UserLogin.as_view(), name='login'),
    path('logout/<int:user_id>', UserLogOut.as_view(), name='logout'),
    path('register', User_Register.as_view()),
    path('api/register/', RegisterAPI.as_view(), name='registerapi'),
    path('api/login/', LoginAPI.as_view(), name='loginapi'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logoutapi'),
    path('api/auth', obtain_auth_token),
] 
