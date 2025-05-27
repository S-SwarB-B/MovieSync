from django.shortcuts import render
from django.http import HttpResponse

def main_screen_no_auth(request):
    return render(request, 'main/MainScreenNoAuth.html')

def all_films_no_auth(request):
    return render(request, 'main/AllFilmsNoAuth.html')

def main_screen(request):
    return render(request, 'main/MainScreen.html')

def all_films(request):
    return render(request, 'main/AllFilms.html')

def favorite(request):
    return render(request, 'main/Favorite.html')

def profile(request):
    return render(request, 'main/Profile.html')

