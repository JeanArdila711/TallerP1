import os
import csv
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Update movie descriptions in the database from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            "--csv",
            dest="csv_file",
            default="updated_movie_descriptions.csv",
            help="CSV file path (default: updated_movie_descriptions.csv in project root)",
        )

    def handle(self, *args, **options):
        csv_file = options.get("csv_file")

        # Si la ruta no es absoluta, la buscamos relativa a la raíz (donde está manage.py)
        if not os.path.isabs(csv_file):
            csv_file = os.path.join(os.getcwd(), csv_file)

        if not os.path.exists(csv_file):
            self.stderr.write(self.style.ERROR(f"CSV file not found: {csv_file}"))
            return

        updated_count = 0
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            # Verificamos que existan las columnas esperadas
            expected = ['Title', 'Updated Description']
            for col in expected:
                if col not in reader.fieldnames:
                    self.stderr.write(self.style.ERROR(f"CSV missing column: '{col}'. Found: {reader.fieldnames}"))
                    return

            for row in reader:
                title = row['Title'].strip()
                new_description = row['Updated Description'].strip()

                try:
                    # Búsqueda tolerante a mayúsculas/minúsculas por si los títulos no coinciden exacto
                    movie_qs = Movie.objects.filter(title__iexact=title)
                    if not movie_qs.exists():
                        # Intento alternativo: buscar por título parcial
                        movie_qs = Movie.objects.filter(title__icontains=title)

                    movie = movie_qs.first()
                    if not movie:
                        self.stderr.write(self.style.WARNING(f"Movie not found: {title}"))
                        continue

                    movie.description = new_description
                    movie.save()
                    updated_count += 1
                    self.stdout.write(self.style.SUCCESS(f"Updated: {movie.title}"))

                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed to update {title}: {str(e)}"))

        self.stdout.write(self.style.SUCCESS(f"Finished updating {updated_count} movies from CSV."))
