from __future__ import unicode_literals

from django.views import generic

from .models import Artist,Piece
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
    return render(request, 'profile.html', context)


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {'message': None})
    template = "profile.html"
    return render(request, template)

def addinfo(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {'message': None})
    template = "Forms/addinfo.html"
    context = {
        'artists': Artist.objects.all(),
    }
    return render(request, template, context)

def search(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {'message': None})
    template = "search.html"
    return render(request, template)


def register(request):
    template = "Registration/register.html"
    return render(request, template)


def artist(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {'message': None})
    template = "artist.html"
    return render(request, template)


def piece(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {'message': None})
    template = "piece.html"
    return render(request, template)

def search(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {'message': None})
    pieces = Piece.objects.all()
    artists = Artist.objects.all()
    return render(request, 'search.html', {'pieces' : pieces,'artists' : artists})

def searchartist(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {'message': None})
    name = request.POST['artist']
    artists = Artist.objects.all()
    return render(request, 'search.html', {'result': Piece.objects.filter(artist__artist_name=name), 'artists': artists})

def searchpiece(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {'message': None})
    piecetitle = request.POST['title']
    artists = Artist.objects.all()
    return render(request, 'search.html', {'result': Piece.objects.filter(piece__title=piecetitle), 'artists': artists})

class artistView(generic.DetailView):
    model = Artist
    template_name = 'artist.html'

class pieceView(generic.DetailView):
    model = Piece
    template_name = 'piece.html'

def delete(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {'message': None})

    message = "Deleted "
    return render(request, 'search.html', {'pieces': Piece.objects.all(), 'artists': Artist.objects.all(), 'message':message})