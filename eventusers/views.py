from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import users
from django.contrib import messages

# Create your views here.

def show_login(request):
    return render(request, 'account.html')

def show_account(request):
    if request.POST and 'register' in request.POST:
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            # Create user accounts
            user=User.objects.create(
            username=username,
            password=password,
            email=email
            )

            users.objects.create(
            user=user,
            phone=phone,
            address=address
            )

        
            return redirect('home')
        except Exception as e:
            error_messages="Duplicate username or invalide credentials"
            messages.error(request,error_messages)
    return render(request, 'signup.html')