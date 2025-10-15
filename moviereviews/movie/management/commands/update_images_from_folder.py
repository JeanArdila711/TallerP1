import os
import unicodedata
import re
from django.core.management.base import BaseCommand
from movie.models import Movie

def normalize_filename(name):
    # Quitar tildes, signos raros y mantener espacios
    name = unicodedata.normalize('NFD', name).encode('ascii', 'ignore').decode('utf-8')
    name = re.sub(r'[^A-Za-z0-9 ]+', '', name)  # solo letras, números y espacios
    name = name.strip()  # deja los espacios
    return name

class Command(BaseCommand):
    help = "Carga las imágenes desde media/movie/images/images/ y actualiza las películas en la base de datos"

    def handle(self, *args, **kwargs):
        images_folder = "../media/movie/images/images/"

        if not os.path.exists(images_folder):
            self.stderr.write(self.style.ERROR(f"La carpeta {images_folder} no existe"))
            return

        movies = Movie.objects.all()
        updated = 0
        not_found = []

        existing_images = set(os.listdir(images_folder))

        for movie in movies:
            normalized_title = normalize_filename(movie.title)
            possible_filename = f"m_{normalized_title}.png"

            match = next((img for img in existing_images if img.lower() == possible_filename.lower()), None)

            if match:
                movie.image = f"movie/images/images/{match}"
                movie.save()
                updated += 1
                self.stdout.write(self.style.SUCCESS(f"✅ Imagen asignada para: {movie.title} → {match}"))
            else:
                not_found.append(movie.title)

        self.stdout.write(self.style.SUCCESS(f"\nTotal de películas actualizadas: {updated}"))
        if not_found:
            self.stdout.write(self.style.WARNING(f"⚠️ Imágenes no encontradas para: {', '.join(not_found)}"))
