"""OfficeMgb URL Configuration
"""
from django.contrib import admin
from django.urls import path

# Import views for handle request
from .views import (
    home_view, user_login_view, user_lougout_view,
    user_register
)

urlpatterns = [
    path('', home_view, name='home'),
    path('login', user_login_view),
    path('logout/<int:user_id>', user_lougout_view),
    path('register', user_register),
] 
