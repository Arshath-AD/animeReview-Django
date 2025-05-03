from django.shortcuts import render
from django.http import FileResponse
import os
from django.conf import settings

# Create your views here.
def home(request):
    return render(request,'myapp/home.html')

def anime_page(request):
    return render(request,'myapp/anime-pages.html')

def index(request):
    return render(request,'myapp/index.html')

def login(request):
    return render(request,'myapp/login.html')

def anirev(request):
    file_path = os.path.join(settings.BASE_DIR, 'myapp', 'static', 'myapp', 'Data', 'action-packed-adventure.json')
    return FileResponse(open(file_path, 'rb'), content_type='application/json')