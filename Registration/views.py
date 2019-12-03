from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'Registration/login.html', {'message' : None})
    context = {'user' : request.user}
    return render(request, 'index.html', context)

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username = username, password = password)
    if user is not  None:
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'Registration/login.html', {'message' : 'Invalid credential'})


def logout_view(request):
    logout(request)
    return render(request, 'Registration/login.html', {'message' : 'Logged out.'})

def show_profile(request):
    if not request.user.is_authenticated:
        return render(request, 'Registration/login.html', {'message': None})
    return render(request, 'Registration/profile.html')

'''@login_required(login_url='/login/')
    def show_profile(request):
    return render(request, 'Registration/profile.html')'''

def create_userold(request):
    username = request.POST['username']
    password = request.POST['password']
    return render(request, 'Registration/login.html', {'message': None})

def create_user(request):
    #This is the method to render the registiration form page and create a new user based on the form data
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # More validation to make sure the above fields are not empty!

        # Validate password1 matched with password2
        # Validate the username and email address was not taken
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                print("Username is taken, must be unique")
                messages.info(request, 'Username is taken, must be unique')
                return render(request, 'Registration/register.html', {'message' : 'Username is taken, must be unique'})
            elif User.objects.filter(email = email).exists():
                print("Email is taken, must be unique")
                messages.info(request, 'Email is taken, must be unique')
                return render(request, 'Registration/register.html', {'message' : 'Email is taken, must be unique'})
            else:
                User.objects.create_user(first_name=first_name, last_name=last_name, email=email,username=username, password=password1)
                print("A user has been created!")
                return render(request, 'Registration/login.html', {'message': 'A user has been created!'})
        else:
            print("Passwords do not match!")
            messages.info(request, 'Passwords do not match!')
            return render(request, 'Registration/register.html', {'message': 'Passwords do not match!'})

        return redirect('index')

    else:
        return render(request, 'Registration/register.html')