from flask import Flask
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect("./netflix.db")
cursor = connection.cursor()
query = """
    SELECT title, release_year, listed_in, description
    FROM netflix
    GROUP BY title, release_year, listed_in, description
    ORDER BY release_year DESC, title
    LIMIT 100
    """

cursor.execute(query)
movie_list = cursor.fetchall()
connection.close()


def get_genre(genre):
    """поиск по жанрy"""
    main_list = []
    for row in movie_list:
        if genre.lower() in row[2].lower():
            result = [{
                "title": row[0],
                "description": row[3]
            }]
            main_list.append(result)
    return main_list


@app.route("/genre/<genre>", methods=['GET'])
def get_movie_by_genre(genre):
    """поиск по жанрy"""
    try:
        movie = ""
        for row in get_genre(genre):
            movie += f"<pre>Title: {row[0]['title']} \n" \
                     f"Description: {row[0]['description']} </pre>"
    except TypeError:
        movie = "Not found"
    return movie


app.run()
