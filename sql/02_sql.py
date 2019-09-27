### This is not the original 02 ###

# Inserting Data

# Refactored the code to include error handling
# changed population to populations to trigger error 

# import SQLite3 library
import sqlite3


# create connection object
conn = sqlite3.connect("new.db")

# create cursor object
cursor = conn.cursor()

# Try
try:
    # execute sql commands with cursor to insert data
    cursor.execute("INSERT INTO populations VALUES('New York City', \
        'NY', 8400000)")
    cursor.execute("INSERT INTO populations VALUES('San Francisco', \
        'CA', 8000000)")

    # commit changes. New command. Do this to save changes before closing connection
    conn.commit()
except:
    print("Ooops! Something went wrong, check your code and try again.")

# close the database connection
conn.close()



