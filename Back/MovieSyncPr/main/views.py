from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>Ура победа тестовый запуск удался.</h4>")
