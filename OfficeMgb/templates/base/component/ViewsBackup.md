@api_view(['POST'])
def user_login_view(request):
    # fetch post data
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        messages.success(request, "Successfully Login")
        login(request, user)
        return redirect('home')
    else:
        messages.error(request, "Invalid Credantial Provided.Please Login Again.")
        return redirect('home')


    # User Logout View 
def user_lougout_view(request, user_id):
    if request.user.id == user_id:
        messages.success(request, "Successfully LogOut")
        logout(request)
        return redirect('home')


    # Creating User Register View 
@api_view(['POST'])
def user_register(request):
#     # Get the post parameter
name = request.POST['name']
username = request.POST['username']
email = request.POST['email']
phone = request.POST['phone']
password = request.POST['password']
confpassword = request.POST['cpassword']

#     # check password confirmation is exit or not
if password != confpassword:
    messages.error(request, "Password is not match to confirm password")
    return redirect('home')

# create user
#     user = User.objects.create_user(username, email, password)
#     user.save()
#     # instance save user profile
#     UserProfile.objects.filter(id=user.id).update(name=name, phone=phone)
#     user = authenticate(request, username=username, password=password)
#     login(request, user)

#     messages.success(request, f"Hii {user} you are succesfully register with Global Services")
#     return redirect('home')