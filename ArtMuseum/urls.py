from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('artist/', views.artist, name='artist'),
    path('piece/', views.piece, name='piece'),
    path('addinfo/', views.addinfo, name='addinfo'),
    path('login/', views.login, name='login'),
]