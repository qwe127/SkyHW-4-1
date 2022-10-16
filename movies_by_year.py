from flask import Flask
import sqlite3

app = Flask(__name__)


@app.route("/movie/<year_from>/to/<year_to>")
def search_by_year(year_from, year_to):
    connection = sqlite3.connect("./netflix.db")
    cursor = connection.cursor()
    query = f"""
        SELECT title, release_year
        FROM netflix
        WHERE release_year BETWEEN {year_from} AND {year_to}
        ORDER BY release_year DESC, title
        LIMIT 1000
        """

    cursor.execute(query)
    movies = ""
    movie_list = cursor.fetchall()
    for row in movie_list:
        movies += f"<pre>Title: {row[0]} Release year: {row[1]}</pre>"

    return f"{movies}"


app.run(debug=True)
