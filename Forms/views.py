from django.shortcuts import render

# Create your views here.
from ArtMuseum.models import Artist, Piece


def add_artist(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {'message': None})
    if request.method == 'POST':
        artist_name = request.POST['artist_name']
        movement = request.POST['movement']
        country = request.POST['country']
        birth_year = request.POST['birth_year']
        death_year = request.POST['death_year']
    if Artist.objects.filter(artist_name=artist_name).exists():
        return render(request, 'Forms/addinfo.html', {'message': 'This artist already exists'})
    a = Artist.objects.create(artist_name=artist_name, movement=movement, country=country,birth_year=birth_year, death_year=death_year)
    return render(request, 'Forms/addinfo.html', {'message': 'Artist Added!'})

def add_piece(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {'message': None})
    if request.method == 'POST':
        artist = request.POST['artist']
        title = request.POST['title']
        type = request.POST['type']
        medium = request.POST['medium']
        picture_url = request.POST['picture_url']
        year = request.POST['year']
    if not Artist.objects.filter(artist_name=artist).exists():
        return render(request, 'Forms/addinfo.html', {'message': "This artist doesn't exist yet so create them first"})
    p = Piece.objects.create(artist=artist, title=title, type=type,medium=medium, picture_url=picture_url,year=year)
    return render(request, 'Forms/addinfo.html', {'message': 'Piece Added!'})

