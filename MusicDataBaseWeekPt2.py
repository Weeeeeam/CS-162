import sqlite3
#connect to my database called Library
con = sqlite3.connect("Library.db")
cur = con.cursor()
#the comment below was the code that created my table in the database
#cur.execute("CREATE TABLE Genre(Genre, City)")
#the next comment was the code that adde values to the tables rows and columns
cur.execute("""
    DELETE FROM Genre WHERE Genre=rock""")

con.commit()