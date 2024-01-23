import sqlite3

db_name = "books.sqlite"
con = sqlite3.connect(db_name)
cur = con.cursor()
cur.execute("""CREATE TABLE user
               (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name TEXT NOT NULL,
                age INT NOT NULL)""")