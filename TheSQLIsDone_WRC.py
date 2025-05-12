import sqlite3
con = sqlite3.connect("Library.db")
cur = con.cursor()
#cur.execute("CREATE TABLE Cities(City, State, Zip)")
#cur.execute("ALTER TABLE Cities RENAME COLUMN new_column TO Population")
#cur.execute("INSERT INTO Cities (City, State, Zip, Population) VALUES (?, ?, ?, ?)",
#             ("Nashville", "TN", "11111", "1500000"))
artist_name = input("Enter the artist name: ")

# SQL query joining three tables and filtering by input
query = '''
SELECT Genre.Genre, Genre.City, Music.Artist, Music.Number_Of_Recordings, Cities.city, Cities.Population
FROM Music
INNER JOIN Genre ON Music.Genre = Genre.Genre
INNER JOIN Cities ON Cities.city = Genre.City
WHERE Music.Artist = ?
'''

# Execute the query with the user's input
cur.execute(query, (artist_name,))

# Fetch and print the result
result = cur.fetchone()
if result:
    # Example output: Rock artist Miley has 14 recordings and is most popular in Los Angeles with a population of 10,000,000
    print(f"{result[0]} artist {result[1]} has {result[2]} recordings and is most popular in {result[3]} with a population of {result[4]}")
else:
    # Try to find the artist anyway (even if genre is not in Genres)
    cur.execute('SELECT Genre, Artist, Number_Of_Recordings FROM Music WHERE Artist = ?', (artist_name,))
    artist_only = cur.fetchone()
    if artist_only:
        print(f"{artist_only[0]} artist {artist_only[1]} has {artist_only[2]} recordings and is popular everywhere")
    else:
        print("No such artist found.")