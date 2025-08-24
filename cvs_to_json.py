import pandas as pd
import json

# Leer archivo csv
df = pd.read_csv(r'movies_initial.csv')

# Guardar DF como Json
df.to_json('movies.json', orient='records')

with open('movies.json', 'r') as file:
    movies = json.load(file)

for i in range(100):
    movie = movies[i]
    print(movie)
    break
