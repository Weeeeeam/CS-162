import sqlite3
#connect to my database called Library
con = sqlite3.connect("Library.db")
cur = con.cursor()
#the comment below was the code that created my table in the database
        #cur.execute("CREATE TABLE Music(Artist, Genre, Number_Of_Recordings)")
#the next comment was the code that adde values to the tables rows and columns
     #cur.execute("""
    #INSERT INTO Music VALUES
        #('Miley', 'Rock', '14'),
        #('Dolly', 'Country', '123'),
        #('Eminem', 'HipHop', '98'),
        #('Brittany', 'Rock', '37')
    #""")
# prints some context
print('The whole table is:')
#selcts whole table and prints all the rows 
cur.execute("SELECT * FROM Music")
rows = cur.fetchall()
for row in rows:
    print(row)
print('The artists in the Rock Genre are:') 
# filters to only take rows where there Genre table say Rock
query = "SELECT * FROM Music WHERE Genre LIKE ?"
cur.execute(query, ('%Rock%',))

# print the rows
rows = cur.fetchall()
for row in rows:
    print(row)