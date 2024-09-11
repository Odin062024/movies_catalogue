from flask import Flask, render_template
import tmdb_client

app = Flask(__name__)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route('/')
def homepage():
    # Pobieramy 8 filmów
    movies = tmdb_client.get_movies(how_many=8)
    return render_template("homepage.html", movies=movies)


@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    # Pobieramy szczegóły filmu i obsadę
    movie = tmdb_client.get_movie_details(movie_id)
    cast = tmdb_client.get_movie_cast(movie_id)
    return render_template("movie_details.html", movie=movie, cast=cast)

if __name__ == '__main__':
    app.run(debug=True)

