import sqlite3

connection = sqlite3.connect("./netflix.db")
cursor = connection.cursor()

query = """
    SELECT title, "cast"
    FROM netflix
    WHERE "cast" LIKE "%Rose McIver%" AND "cast" LIKE '%Ben Lamb%'
    GROUP BY title, "cast"
    ORDER BY release_year DESC, title
    """

cursor.execute(query)
movie_list = cursor.fetchall()

same_movie_count = 0
for row in movie_list:
    if "Rose McIver" and "Ben Lamb" in row[1]:
        same_movie_count += 1

print(f"Rose McIver, Ben Lamb both appeared in the same movies: {same_movie_count} times.")

