from flask import Flask
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect("./netflix.db")
cursor = connection.cursor()
query = """
    SELECT title, country, release_year, listed_in, description
    FROM netflix
    ORDER BY release_year DESC, title
    LIMIT 100
    """

cursor.execute(query)
movie_list = cursor.fetchall()
connection.close()

for row in movie_list:
    print(row[0])


def get_movie_dict(title):
    """поиск по названию"""
    result = "Not found"
    for row in movie_list:
        if row[0].lower() in title.lower():
            result = {
                "title": row[0],
                "country": row[1],
                "release_year": str(row[2]),
                "genre": row[3],
                "description": row[4]
            }
    return result


@app.route("/movie/<title>", methods=['GET'])
def movie_title(title):
    """поиск по названию"""
    try:
        movie = ""
        movie += f"<pre>Title: {get_movie_dict(title)['title']} \n" \
                 f"Country: {get_movie_dict(title)['country']} \n" \
                 f"Release year: {get_movie_dict(title)['release_year']} \n" \
                 f"Genre: {get_movie_dict(title)['genre']} \n" \
                 f"Description: {get_movie_dict(title)['description']} </pre>"
    except TypeError:
        movie = "Not found"
    return movie


app.run(debug=True)
