from django.shortcuts import render
from ArtMuseum.models import Artist, Piece
from .forms import ArtistForm, PieceForm


def add_artist(request):
    if not request.user.is_authenticated:
        return render(request, 'Registration/login.html', {'message': None})

    if request.method == 'POST':
        artist_name = request.POST['artist_name']
        movement = request.POST['movement']
        country = request.POST['country']
        birth_year = request.POST['birth_year']
        death_year = request.POST['death_year']

        if artist_name == "" or movement == "" or country == "" or birth_year == 0 or death_year == 0:
            return render(request, 'Forms/addinfo.html',{'message': "One of the inputs was empty!", 'artists': Artist.objects.all()})

        if Artist.objects.filter(artist_name=artist_name).exists():
            return render(request, 'Forms/addinfo.html',{'message': 'This artist already exists', 'artists': Artist.objects.all()})

        a = Artist.objects.create(artist_name=artist_name, movement=movement, country=country, birth_year=birth_year, death_year=death_year)
        return render(request, 'Forms/addinfo.html', {'message': 'Artist Added!', 'artists': Artist.objects.all()})
    return render(request, 'Forms/addinfo.html', {'message': None, 'artists': Artist.objects.all()})

def add_piece(request):
    if not request.user.is_authenticated:
        return render(request, 'Registration/login.html', {'message': None})

    if request.method == 'POST':
        artist = request.POST['artist']
        title = request.POST['title']
        type = request.POST['type']
        medium = request.POST['medium']
        picture_url = request.POST['picture_url']
        year = request.POST['year']

        if artist == "" or title == "" or type == "" or medium == "" or picture_url == "" or year == 0:
            return render(request, 'Forms/addinfo.html',{'message': "One of the inputs was empty!", 'artists': Artist.objects.all()})

        if not Artist.objects.filter(artist_name=artist).exists():
            return render(request, 'Forms/addinfo.html',{'message': "This artist doesn't exist yet so create them first",'artists': Artist.objects.all()})

        p = Piece.objects.create(artist=Artist.objects.get(artist_name=artist), title=title, type=type, medium=medium,picture_url=picture_url, year=year)
        return render(request, 'Forms/addinfo.html', {'message': 'Piece Added!', 'artists': Artist.objects.all()})
    return render(request, 'Forms/addinfo.html', {'message': None, 'artists': Artist.objects.all()})


