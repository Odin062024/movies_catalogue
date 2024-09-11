import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMDJiMDQxNTg3NzYxMjIxNTE0MWU3MDlhMWIzMTFiZiIsIm5iZiI6MTcyNTk5MjQ2MS40NzM3ODksInN1YiI6IjY2ZTA0OGZmNzE4OGM5OWZiOTI4ZTNmNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mAe2nxB0avLMS9MEys-iPJgo74lQBVF27GL7uwYzhCQ"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]
