from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    #template = "Registration/login.html"
    #return render(request, template)
    if not request.user.is_authenticated:
        return render(request, 'Registration/login.html', {'message' : None})
    context  = {'user' : request.user}
    return render(request, 'index.html', context)


def index(request):
    template = "index.html"
    return render(request, template)

def addinfo(request):
    template = "Forms/addinfo.html"
    return render(request, template)

def search(request):
    template = "search.html"
    return render(request, template)


def register(request):
    template = "Registration/register.html"
    return render(request, template)


def artist(request):
    template = "artist.html"
    return render(request, template)


def piece(request):
    template = "piece.html"
    return render(request, template)
