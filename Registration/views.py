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

from .forms import RegistrationForm

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
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                if User.objects.filter(username=request.POST['username']).exists():
                    return render(request, 'Registration/register.html', {'message': 'Username is taken, must be unique'})
                elif User.objects.filter(email = request.POST['email']).exists():
                    return render(request, 'Registration/register.html', {'message' : 'Email is taken, must be unique'})
                else:
                    form.save()
                    return render(request, 'Registration/login.html', {'message': 'A user has been created!'})
            else:
                return render(request, 'Registration/register.html', {'message': 'Passwords do not match!'})

        else:
            return render(request, 'Registration/register.html')
