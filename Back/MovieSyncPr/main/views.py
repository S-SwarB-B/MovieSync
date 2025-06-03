from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import UpdateUserForm
from .models import Films
from accounts.models import Users
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required 


class FilsDetailView(DetailView):
    model = Films
    template_name = 'main/FilmCard.html'
    context_object_name = 'film'

def main_screen_no_auth(request):
    films = Films.objects.all()
    return render(request, 'main/MainScreenNoAuth.html', {'films': films})

def all_films_no_auth(request):
    films = Films.objects.all()
    return render(request, 'main/AllFilmsNoAuth.html', {'films': films})

@login_required(login_url="accounts:login")
def main_screen(request):
    if request.user.is_authenticated: 
        films = Films.objects.all()
        return render(request, 'main/MainScreen.html', {'films': films})
    
@login_required(login_url="accounts:login")
def all_films(request):
    films = Films.objects.all()
    return render(request, 'main/AllFilms.html', {'films': films})

@login_required(login_url="accounts:login")
def favorite(request):
    return render(request, 'main/Favorite.html')

@login_required(login_url="accounts:login")
def profile(request, profile_id):

    if request.user.id != profile_id:
        profile_id = request.user.id
    

    profile_ = get_object_or_404(get_user_model(), pk=profile_id)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=profile_)
        if form.is_valid():
            form.save()
            return redirect('profile', profile_id = profile_id)
    else:
        form = UpdateUserForm(instance=profile_)

    data = {
        'profile': profile_,
        'form': form,
    }
    return render(request, 'main/Profile.html', data)

def film(request):
    picture = Films.objects.all()
    return render(request, 'main/FilmCard.html', {
        'picture': picture,
    })


def movie_search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        films = Films.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )[:10]

        results = [
            {
                'id': film.id,
                'title': film.title,
                'picture': film.picture.url if film.picture else None,
                'rating': film.rating,
            }
            for film in films
        ]
    return JsonResponse({'results': results})

