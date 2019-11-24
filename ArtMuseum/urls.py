from django.urls import path, include
from . import views
from Registration import views as viewsR

urlpatterns = [
    path('', viewsR.index, name='start'),
    path('index/', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('artist/', views.artist, name='artist'),
    path('piece/', views.piece, name='piece'),
    path('addinfo/', views.addinfo, name='addinfo'),
    path('', include('Registration.urls'), name='Registration'),
    path('', include('Forms.urls'), name='Forms'),
]