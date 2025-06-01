from django.shortcuts import render, get_object_or_404

from accounts.models import Users


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

def profile(request, profile_id):
    profile_ = get_object_or_404(Users, pk=profile_id)
    data = {
        'profile': profile_
    }
    return render(request, 'main/Profile.html', data)

def film(request):
    return render(request, 'main/FilmCard.html')

