from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    number_of_movies = 10  # Możesz zmienić tę wartość na dowolną liczbę
    movies = [f"Film {i+1}" for i in range(number_of_movies)]  # Generuje listę filmów
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)