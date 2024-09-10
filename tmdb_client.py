import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMDJiMDQxNTg3NzYxMjIxNTE0MWU3MDlhMWIzMTFiZiIsIm5iZiI6MTcyNTk5MjQ2MS40NzM3ODksInN1YiI6IjY2ZTA0OGZmNzE4OGM5OWZiOTI4ZTNmNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mAe2nxB0avLMS9MEys-iPJgo74lQBVF27GL7uwYzhCQ"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

# Uruchomienie funkcji i przypisanie wyniku
movies_data = get_popular_movies()

# Wyświetlenie zawartości
print(movies_data)

if __name__ == "__main__":
    popular_movies = get_popular_movies()
    print(popular_movies)
