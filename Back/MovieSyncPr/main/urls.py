from django.urls import path
from .import views
urlpatterns = [
    path('', views.main_screen_no_auth, name='main_screen_no_auth'),
    path('AllFilmsNoAuth', views.all_films_no_auth, name='all_films_no_auth'),
    path('MainScreen', views.main_screen, name='main_screen'),
    path('AllFilms', views.all_films, name='all_films'),
    path('Favorite', views.favorite, name='favorite'),
    path('Profile', views.profile, name='profile'),
]