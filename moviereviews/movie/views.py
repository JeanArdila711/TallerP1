from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

# Create your views here.

def home(request):
    searchTerm = request.GET.get('searchMovie')

    # Si se busca una película
    if searchTerm:
        # Lista unicamente las películas cuyo título tiene el nombre buscado
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        # Lista todas las películas de las bases de datos
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies':movies})

# Función para about
def about(request):

    # Uso de plantilla sin parámetros
    return render(request, 'about.html')