# Homework, joining the 2 tables in the cars database
# to print out invoices of when each car was sold
# Make Model
# Quantity
# SellDates on extra lines

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # Select the relevant fields I wanted from the 2 tables, and join them together
    # NOTE: I messed up the orders table, make field is technicaly a model, which is why
    #   the Join looks messed up
    c.execute("""SELECT DISTINCT inventory.make, inventory.model,
                inventory.inventory, orders.make, orders.selldate 
                FROM inventory, orders 
                WHERE inventory.model = orders.make ORDER BY inventory.model ASC
            """)

    # get the results
    rows = c.fetchall()

    # offset counter so you dont get duplicate models in the result
    z = -1

    for r in rows:
        # Compare the model to the previous row, so I'm not printing the same model multiple times.
        if rows[z][1] == r[1]:
            z = z + 1
            continue

        # Printing the report
        # Make Model
        # Quantity
        # Sell dates
        print(r[0], r[1])
        print("Quantity: " + str(r[2]))
        for s in rows:
            if s[1] == r[1]:
                print("  Dates Sold: "+s[4])
        z = z + 1

        