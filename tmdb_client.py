import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMDJiMDQxNTg3NzYxMjIxNTE0MWU3MDlhMWIzMTFiZiIsIm5iZiI6MTcyNTk5MjQ2MS40NzM3ODksInN1YiI6IjY2ZTA0OGZmNzE4OGM5OWZiOTI4ZTNmNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mAe2nxB0avLMS9MEys-iPJgo74lQBVF27GL7uwYzhCQ"

def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_popular_movies():
    return call_tmdb_api("movie/popular")

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type='popular'):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")

def get_movie_details(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")

def get_movie_cast(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/credits")["cast"]


