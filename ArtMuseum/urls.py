from django.urls import path, include
from . import views
from Registration import views as viewsR

urlpatterns = [
    path('', viewsR.index, name='start'),
    path('index/', views.index, name='index'),
    path('search/', views.query, name='search'),
    path('register/', views.register, name='register'),
    path('<int:pk>/artist/', views.artistView.as_view(), name='artist'),
    path('<int:pk>/piece/', views.pieceView.as_view(), name='piece'),
    path('addinfo/', views.addinfo, name='addinfo'),
    path('', include('Registration.urls'), name='Registration'),
    path('', include('Forms.urls'), name='Forms'),
    path('delete/',views.delete, name='delete')
]