from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView  
from django.views import View

# Create your views here.
def home_view(request, *args):
    return render(request, 'pages/home.html')

# Creating User Login View 
class UserLogin(LoginView):
    template_name = 'base/component/login.html'

# User Logout View 
class UserLogOut(LogoutView):
    template_name = 'pages/home.html'

# User Registration
class User_Register(View):

    def post(self, request, *args):
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confpassword = request.POST['cpassword']

        # check password confirmation is exit or not
        if password != confpassword:
            messages.error(request, "Password is not match to confirm password")
            return redirect('home')

        # create user
        user = User.objects.create_user(username, email, password)
        user.save()
        # instance save user profile
        print(f'Immedid {user.id}')
        UserProfile.objects.filter(user=user).update(name=name, phone=phone)
        user = authenticate(request, username=username, password=password)
        login(request, user)

        messages.success(request, f"Hii {user} you are succesfully register with Global Services")
        return redirect('home')
