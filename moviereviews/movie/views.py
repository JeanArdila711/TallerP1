from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
import matplotlib.pyplot as plt
import matplotlib
import io, base64, re
import urllib, base64
from collections import Counter

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

def statistics_view(request):
    matplotlib.use("Agg")
    all_movies = Movie.objects.all()

    # ---------------------------
    # 1. Películas por año
    # ---------------------------
    movies_counts_by_year = {}
    for movie in all_movies:
        year = movie.year if movie.year else "None"
        movies_counts_by_year[year] = movies_counts_by_year.get(year, 0) + 1

    bar_positions = range(len(movies_counts_by_year))
    plt.bar(bar_positions, movies_counts_by_year.values(), width=0.5, align="center")
    plt.title("Movies per year")
    plt.xlabel("Year")
    plt.ylabel("Number of movies")
    plt.xticks(bar_positions, movies_counts_by_year.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.3)

    buffer1 = io.BytesIO()
    plt.savefig(buffer1, format="png", bbox_inches="tight")
    buffer1.seek(0)
    graphic_year = base64.b64encode(buffer1.read()).decode("utf-8")
    buffer1.close()
    plt.close()

    # ---------------------------
    # 2. Películas por género
    # ---------------------------
    raw_genres = Movie.objects.values_list("genre", flat=True)
    first_genres = []
    for g in raw_genres:
        if not g:
            continue
        first = re.split(r"[,/|;]+", str(g))[0].strip()
        if first:
            first_genres.append(first)

    counts = Counter(first_genres)
    labels = list(counts.keys())
    values = [counts[l] for l in labels]

    fig, ax = plt.subplots()
    if values:
        ax.bar(labels, values)
        ax.set_title("Películas por género (primer género)")
        ax.set_xlabel("Género")
        ax.set_ylabel("Cantidad")
        ax.tick_params(axis="x", rotation=45, labelsize=9)
        fig.tight_layout()
    else:
        ax.text(0.5, 0.5, "Sin datos para graficar", ha="center", va="center")
        ax.axis("off")

    buffer2 = io.BytesIO()
    plt.savefig(buffer2, format="png", bbox_inches="tight")
    buffer2.seek(0)
    graphic_genre = base64.b64encode(buffer2.read()).decode("utf-8")
    buffer2.close()
    plt.close(fig)

    # ---------------------------
    # Renderizar ambas gráficas
    # ---------------------------
    return render(
        request,
        "statistics.html",
        {"graphic_year": graphic_year, "graphic_genre": graphic_genre},
    )

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})