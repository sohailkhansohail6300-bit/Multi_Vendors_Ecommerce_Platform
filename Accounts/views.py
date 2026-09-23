from django.contrib import messages
from django.shortcuts import render,redirect
from .models import userprofile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.

def Account_cards(request):
    return render(request,'accounts/accounts_page.html')

def Signup(request):
    if request.method == 'POST':
        a = request.POST
        name = a.get('full_name')
        email = a.get('email')
        shop_details = a.get('shop_details')
        image = request.FILES.get('image')
        pass1 = a.get('pass1')
        pass2 = a.get('pass2')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'accounts/signup.html')
        elif not name or len(name) < 4:
            messages.error(request, "Username must be at least 4 characters long.")
            return render(request, 'accounts/signup.html')
        elif not name.isalpha():
             messages.error(request, "Username must contain only letters. Do not add digits.")
        elif User.objects.filter(username=name).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'accounts/signup.html')
        elif not email or User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, 'accounts/signup.html')
        elif not shop_details or not shop_details.strip():
            messages.error(request, "Shop details cannot be empty.")
            return render(request, 'accounts/signup.html')
        else:
            user = User.objects.create_user(username=name, email=email, password=pass1)
            user.save()
            user_profile = userprofile(user_profile_relation=user, shop_detail=shop_details, image=image)
            user_profile.save()
            
            messages.success(request, "Your account has been created successfully!")
            return redirect('accounts:login')

    return render(request, 'accounts/signup.html')

def Login_E(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('userProfile:user_profile')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'accounts/login.html')
    return render(request,'accounts/login.html')