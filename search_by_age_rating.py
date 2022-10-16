from flask import Flask
import sqlite3


def make_list(movie_list):
    main_list = []
    for row in movie_list:
        result = [{
            "title": row[0],
            "rating": row[1],
            "description": row[2]
        }]
        main_list.append(result)
    str_list = ""
    for row in main_list:
        str_list += f"Title: {row[0]['title']}<pre>Rating: {row[0]['rating']}</pre><pre>Description: {row[0]['description']}</pre>"
    return str_list


app = Flask(__name__)

connection = sqlite3.connect('netflix.db')
cursor = connection.cursor()

query_G = """
    SELECT title, rating, description
    FROM netflix
    WHERE rating LIKE "G%"
    GROUP BY title, rating, description
    ORDER BY rating, title
    """
query_PG = """
    SELECT title, rating, description
    FROM netflix
    WHERE rating LIKE "PG%"
    GROUP BY title, rating, description
    ORDER BY rating, title
    """
query_R = """
    SELECT title, rating, description
    FROM netflix
    WHERE rating LIKE "R"
    GROUP BY title, rating, description
    ORDER BY rating, title
    """
query_NC_17 = """
    SELECT title, rating, description
    FROM netflix
    WHERE rating LIKE "NC-17"
    GROUP BY title, rating, description
    ORDER BY rating, title
    """

G_movies = cursor.execute(query_G)
G_movies_str = make_list(G_movies)

PG_movies = cursor.execute(query_PG)
PG_movies_str = make_list(PG_movies)

R_movies = cursor.execute(query_R)
R_movies_str = make_list(R_movies)

NC_17_movies = cursor.execute(query_NC_17)
NC_17_movies_str = make_list(NC_17_movies)


@app.route("/rating/adult")
def adult_movies():
    movies = ""
    movies += R_movies_str
    movies += NC_17_movies_str
    return movies


@app.route("/rating/family")
def family_movies():
    movies = ""
    movies += G_movies_str
    movies += PG_movies_str
    return movies


@app.route("/rating/children")
def children_movies():
    movies = ""
    movies += G_movies_str
    return movies


app.run(debug=True)
