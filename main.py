from flask import Flask, render_template, request
import tmdb_client
from flask import request

app = Flask(__name__)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route('/')
def homepage():
    available_lists = ['popular', 'top_rated', 'upcoming', 'now_playing']
    selected_list = request.args.get('list_type', 'popular')
    if selected_list not in available_lists:
        return redirect(url_for('homepage', list_type='popular'))
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", 
                           movies=movies, 
                           current_list=selected_list, 
                           available_lists=available_lists)

@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    movie = tmdb_client.get_movie_details(movie_id)
    cast = tmdb_client.get_movie_cast(movie_id)
    return render_template("movie_details.html", movie=movie, cast=cast)

if __name__ == '__main__':
    app.run(debug=True)

