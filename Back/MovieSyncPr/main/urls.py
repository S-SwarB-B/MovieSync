from django.urls import path
from .import views
urlpatterns = [
    path('', views.main_screen_no_auth, name='main_screen_no_auth'),
    path('AllFilmsNoAuth', views.all_films_no_auth, name='all_films_no_auth'),
]