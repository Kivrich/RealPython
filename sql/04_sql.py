# import from CSV into Database

# import csv library and sqlite3
import csv
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # open the csv file and assign it to a variable
    employees = csv.reader(open("employees.csv", "rU"))

    # create a new table named employees
    c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

    # insert data into table
    c.executemany("INSERT INTO employees(firstname, lastname) values (?, ?)", employees)



