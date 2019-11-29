from django.urls import path
from . import views

urlpatterns = [
    path('addartist/', views.add_artist, name='addartist'),
    path('addpiece/', views.add_piece, name='addpiece'),
    path('search/', views.search, name='search'),
]