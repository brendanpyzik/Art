from django import forms
from ArtMuseum.models import Artist, Piece


class ArtistForm(forms.Form):
    artist_name = forms.CharField(required=True, max_length=200)
    movement = forms.CharField(required=True, max_length=200)
    country = forms.CharField(required=True, max_length=200)
    birth_year = forms.IntegerField(required=True, default=0)
    death_year = forms.IntegerField(required=False)


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['artist_name', 'movement', 'country', 'birth_year', 'death_year']