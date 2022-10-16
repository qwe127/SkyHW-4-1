import json
import sqlite3

connection = sqlite3.connect("./netflix.db")
cursor = connection.cursor()

query = """
    SELECT type, title, release_year, listed_in, description
    FROM netflix
    GROUP BY title, release_year, listed_in, description
    ORDER BY release_year DESC, title
    LIMIT 100
    """

cursor.execute(query)
movie_list = cursor.fetchall()

for row in movie_list:
    print(row)

json_file = []

for row in movie_list:
    main_list = {
        "type": row[0],
        "title": row[1],
        "release_year": row[2],
        "genre": row[3],
        "description": row[4]
    }
    json_file.append(main_list)


out_file = open('json_list.json', 'w')
json.dump(json_file, out_file)
