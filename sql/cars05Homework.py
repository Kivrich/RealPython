# Creating a new table for cars.db
# Add 15 records, 3 for each car.
# Each record is an order date, format YYYY-MM-DD

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # create a tuple of information with Model and YearSold
    cars = [
        ("Mustang", "2012-02-12"),
        ("Mustang", "2017-08-26"),
        ("Mustang", "2005-06-04"),
        ("Civic", "2018-06-22"),
        ("Civic", "2011-01-28"),
        ("Civic", "2013-10-09"),
        ("CRX", "2019-03-21"),
        ("CRX", "2018-12-28"),
        ("CRX", "2016-04-01"),
        ("Pinto", "1978-04-15"),
        ("Pinto", "1990-07-13"),
        ("Pinto", "1984-02-30"),
        ("Shelby", "2008-05-22"),
        ("Shelby", "2000-11-26"),
        ("Shelby", "2003-06-22"),
    ]

    # create the new table
    c.execute("CREATE TABLE orders(make, selldate)")

    # populate data from cars tuple
    c.executemany("INSERT INTO orders VALUES(?, ?)", cars)