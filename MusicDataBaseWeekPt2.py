import sqlite3
#connect to my database called Library
con = sqlite3.connect("Library.db")
cur = con.cursor()
#the comment below was the code that created my table in the database
#cur.execute("CREATE TABLE Genre(Genre, City)")
#the next comment was the code that adde values to the tables rows and columns
#cursor.execute("INSERT INTO table_name (column1, column2) VALUES (?, ?)", (value1, value2))
#cur.execute("INSERT INTO Genre (Genre, City) VALUES (?, ?)",
            #('Opera', 'Florence'))
# Connect to the SQLite database 
# Write your INNER JOIN SQL query
query = '''
SELECT Music.Artist
FROM Music
INNER JOIN Genre ON Music.Genre = Genre.Genre
'''
cur.execute(query)
results = cur.fetchall()
# Process or print the results
for row in results:
    print(row)
#con.commit()
