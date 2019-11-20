from django.conf.urls import url
from . import views

urlpatterns = [

    url('', views.index, name='index'),
    url('login/', views.login_view, name='login'),
    url('logout/', views.logout_view, name='logout'),
    url('profile/', views.show_profile, name='profile'),
]
