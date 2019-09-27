# Insert 5 cars into the inventory table
# 3 Fords, and 2 Hondas

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # create a tuple of information, then executemany
    cars = [
        ("Ford", "Mustang", 5),
        ("Honda", "Civic", 12),
        ("Honda", "CRX", 3),
        ("Ford", "Pinto", 21),
        ("Ford", "Shelby", 1),
    ]

    c.executemany("INSERT INTO inventory(make, model, inventory) VALUES(?, ?, ?)", cars)

