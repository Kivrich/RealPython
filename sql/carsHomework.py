# SQL Homework. Create a cars databse with an inventory table that
# holds the cars make, model, and inventory. With appropriate types

#import sqlite 
import sqlite3

#create database
conn = sqlite3.connect("cars.db")

#create cursor
cursor = conn.cursor()

#create database
cursor.execute("""CREATE TABLE inventory
                (make TEXT, model TEXT, inventory INT)
                """)

#close database
conn.close()