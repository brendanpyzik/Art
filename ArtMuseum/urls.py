from django.urls import path, include
from . import views
from Registration import views as viewsR

urlpatterns = [
    path('', viewsR.index, name='start'),
    path('index/', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('query/', views.query, name='query'),
    path('register/', views.register, name='register'),
    path('<int:pk>/artist/', views.artistView.as_view(), name='artist'),
    path('<int:pk>/piece/', views.pieceView.as_view(), name='piece'),
    path('addinfo/', views.addinfo, name='addinfo'),
    path('', include('Registration.urls'), name='Registration'),
    path('', include('Forms.urls'), name='Forms'),
    path('deletepiece/', views.deletePiece, name='delete')
]