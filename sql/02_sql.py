# Inserting Data

# import SQLite3 library
import sqlite3


# create connection object
conn = sqlite3.connect("new.db")

# create cursor object
cursor = conn.cursor()

# execute sql commands with cursor to insert data
cursor.execute("INSERT INTO population VALUES('New York City', \
    'NY', 8400000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', \
    'CA', 8000000)")

# commit changes. New command. Do this to save changes before closing connection
conn.commit()

# close the database connection
conn.close()



