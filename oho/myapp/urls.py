from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  #maps to home.html
    path('anime-pages.html',views.anime_page, name='anime-pages'),
    path('index.html',views.index, name='index'),
    path('home.html',views.home, name='home'),
    path('login.html',views.login, name='login'),
    path('HTML/anime-pages.html',views.anime_page, name='anime-pages'),
    path('Data/action-packed-adventure.json',views.anirev, name="action-packed-adventure")
] 