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

def query(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {'message': None})
    find = request.POST['find']
    found_artists = Artist.objects.filter(artist_name__contains=find)
    found_artist_pieces = Piece.objects.filter(artist__artist_name__contains=find)
    found_pieces = Piece.objects.filter(title__contains=find)
    return render(request, 'search.html', {'message' : 'Results', 'found_pieces': found_pieces, 'found_artists': found_artists, 'found_artist_pieces': found_artist_pieces})


class artistView(generic.DetailView):
    model = Artist
    template_name = 'artist.html'


class pieceView(generic.DetailView):
    model = Piece
    template_name = 'piece.html'
