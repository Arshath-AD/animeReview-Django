from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  #maps to home.html
    path('anime-pages.html',views.anime_page, name='anime-pages'),
    path('index.html',views.index, name='index'),
    path('home.html',views.home, name='home'),
    path('HTML/anime-pages.html',views.anime_page, name='anime-pages'),
    path('Data/action-packed-adventure.json',views.anirev, name="action-packed-adventure"),
    #for registeration and login:
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]