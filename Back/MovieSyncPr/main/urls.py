from django.urls import path
from .import views
urlpatterns = [
    path('', views.main_screen_no_auth, name='main_screen_no_auth'),
    path('AllFilmsNoAuth/', views.all_films_no_auth, name='all_films_no_auth'),
    path('MainScreen/', views.main_screen, name='main_screen'),
    path('AllFilms/', views.all_films, name='all_films'),
    path('Favorite/', views.favorite, name='favorite'),
    path('search/', views.movie_search, name='movie_search'),
    path('Profile/<int:profile_id>', views.profile, name='profile'),
    #path('Film/', views.film, name='film'),
    path('<int:pk>', views.FilsDetailView.as_view(), name='film_detail'),
    path('films/<int:pk>/add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
    path('films/<int:pk>/remove_from_favorites/', views.remove_from_favorites, name='remove_from_favorites'),
]