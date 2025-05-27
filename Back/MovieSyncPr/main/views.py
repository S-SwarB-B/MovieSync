from django.shortcuts import render
from django.http import HttpResponse

def main_screen_no_auth(request):
    return render(request, 'main/MainScreenNoAuth.html')

def all_films_no_auth(request):
    return render(request, 'main/AllFilmsNoAuth.html')

