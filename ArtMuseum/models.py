from django.db import models

# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=200)
    movement = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    birth_year = models.IntegerField(default=0)
    death_year = models.IntegerField(default=0)

    def __str__(self):
        return self.artist_name

class Piece(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    medium = models.CharField(max_length=200)
    picture_url = models.CharField(max_length=500)
    year = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} by {self.artist}"






