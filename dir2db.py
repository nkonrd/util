import os
import sqlite3

folder = r"."
items = [(item,) for item in os.listdir(folder)]

if os.path.isfile('items.db'):
	os.remove('items.db')

connection = sqlite3.connect('items.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE items (name text)")

cursor.executemany('INSERT INTO items VALUES (?)', items)
connection.commit()
connection.close()
