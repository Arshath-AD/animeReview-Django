from django.shortcuts import render, redirect
from django.http import FileResponse
from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
import os

# Create your views here.
# accounts/views.py     

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # hashing password
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'myapp/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'myapp/login.html', {'error': 'Invalid credentials'})
    return render(request, 'myapp/login.html')

@login_required
def dashboard_view(request):
    return render(request, 'myapp/dashboard.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')

# =============================================================================

def home(request):
    return render(request, 'myapp/home.html')

def anime_page(request):
    return render(request, 'myapp/anime-pages.html')

def login_page(request):
    return render(request, 'myapp/login.html')

def index(request):
    return render(request, 'myapp/index.html')

def anirev(request):
    file_path = os.path.join(settings.BASE_DIR, 'myapp', 'static', 'myapp', 'Data', 'action-packed-adventure.json')
    return FileResponse(open(file_path, 'rb'), content_type='application/json')
