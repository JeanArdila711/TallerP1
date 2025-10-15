import numpy as np
from django.core.management.base import BaseCommand
from movie.models import Movie
import random

class Command(BaseCommand):
    help = "Show embedding values for a random movie"

    def handle(self, *args, **kwargs):
        movies = list(Movie.objects.all())
        if not movies:
            self.stdout.write("No movies found in the database.")
            return

        movie = random.choice(movies)
        emb = np.frombuffer(movie.emb, dtype=np.float32)
        self.stdout.write(f"🎬 {movie.title}")
        self.stdout.write(f"🔢 First 10 values of embedding: {emb[:10]}")
        self.stdout.write(f"📏 Embedding length: {len(emb)}")
