# Update the quantity on two of the records, 
# and then output all of the records from the table

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    #update quantity
    c.execute("UPDATE inventory SET inventory = 2 WHERE model = 'CRX'")

    # Select Statement
    c.execute("SELECT * FROM inventory")

    #get rows of SELECT STATEMENT to print
    rows = c.fetchall()
    
    for r in rows:
        print(r[0], r[1], r[2])
    