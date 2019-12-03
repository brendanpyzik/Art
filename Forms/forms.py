from django import forms
from ArtMuseum.models import Artist, Piece
from ArtMuseum import models


class ArtistForm(forms.Form):
    artist_name = forms.CharField(required=True, max_length=200)
    movement = forms.CharField(required=True, max_length=200)
    country = forms.CharField(required=True, max_length=200)
    birth_year = forms.IntegerField(required=True)
    death_year = forms.IntegerField(required=False)


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['artist_name', 'movement', 'country', 'birth_year', 'death_year']


class PieceForm(forms.Form):
    artist_name = forms.CharField(required=True, max_length=200)
    title = forms.CharField(required=True, max_length=200)
    type = forms.CharField(required=True, max_length=200)
    medium = forms.CharField(required=True, max_length=200)
    picture_url = forms.CharField(required=True, max_length=500)
    year = forms.CharField(required=False)


class PieceForm(forms.ModelForm):
    class Meta:
        model = Piece
        fields = ['artist', 'title', 'type', 'medium', 'picture_url', 'year']
