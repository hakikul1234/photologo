from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, PhotoForm
from .models import Photo

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def main_page(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
    else:
        form = PhotoForm()
    photos = Photo.objects.filter(user=request.user)
    return render(request, 'main.html', {'form': form, 'photos': photos})

def user_logout(request):
    logout(request)
    return redirect('login')
