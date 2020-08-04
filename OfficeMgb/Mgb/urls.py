"""OfficeMgb URL Configuration
"""
from django.contrib import admin
from django.urls import path

# Import views for handle request
from .views import (
    home_view, User_Register, UserLogin, 
    UserLogOut
)

urlpatterns = [
    path('', home_view, name='home'),
    path('login', UserLogin.as_view(), name='login'),
    path('logout/<int:user_id>', UserLogOut.as_view(), name='logout'),
    path('register', User_Register.as_view()),
] 
