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
        return render(request, 'registration/login.html', {'message' : None})
    context  = {'user' : request.user}
    return render(request, 'registration/user.html', context)

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username = username, password = password)
    if user is not  None:
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'registration/login.html', {'message' : 'Invalid credential'})


def logout_view(request):
    logout(request)
    return render(request, 'registration/login.html', {'message' : 'Logged out.'})

def show_profile(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {'message': None})
    return render(request, 'registration/profile.html')

'''@login_required(login_url='/login/')
def show_profile(request):
    return render(request, 'simple_authentication/profile.html')'''
