from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'myapp/home.html')

def anime_page(request):
    return render(request,'myapp/anime-pages.html')

def index(request):
    return render(request,'myapp/index.html')

def login(request):
    return render(request,'myapp/login.html')