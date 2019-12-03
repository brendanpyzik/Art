from django.shortcuts import render
from ArtMuseum.models import Artist
from .forms import ArtistForm, PieceForm


def add_artist(request):
    if not request.user.is_authenticated:
        return render(request, 'Registration/login.html', {'message': None})

    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Forms/addinfo.html', {'message': 'Artist added!', 'artists': Artist.objects.all()})
        return render(request, 'Forms/addinfo.html', {'message': "Your input was invalid. Try again.", 'artists': Artist.objects.all()})


def add_piece(request):
    if not request.user.is_authenticated:
        return render(request, 'Registration/login.html', {'message': None})

    if request.method == 'POST':
        form = PieceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Forms/addinfo.html', {'message': 'Piece Added!', 'artists': Artist.objects.all()})
    return render(request, 'Forms/addinfo.html', {'message': "Your input was invalid. Try again.", 'artists': Artist.objects.all()})



