from django.core.management.base import BaseCommand
from movie.models import Movie
from openai import OpenAI
import os
from dotenv import load_dotenv

# Carga variables del archivo .env
load_dotenv('C:\Users\jeanc\OneDrive\Documentos\GitHub\moviereviewsproject\openAI.env')

# Inicializa el cliente OpenAI
client = OpenAI(api_key=os.environ.get('openai_apikey'))

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content.strip()

class Command(BaseCommand):
    help = "Actualiza las descripciones de las películas usando la API de OpenAI"

    def handle(self, *args, **kwargs):
        movies = Movie.objects.all()
        instruction = "Mejora o reescribe la descripción de la película de forma atractiva y profesional."

        for movie in movies:
            prompt = f"{instruction} Actualiza la descripción '{movie.description}' de la película '{movie.title}'."
            response = get_completion(prompt)
            movie.description = response
            movie.save()
            print(f"✅ Descripción actualizada para: {movie.title}")
            break  # Solo actualiza la primera película
