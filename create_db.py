import sqlite3

connect_to_db = sqlite3.connect("expenses.db")

set_cursor = connect_to_db.cursor()

set_cursor.execute("""CREATE TABLE IF NOT EXISTS expenses
(id INTEGER PRIMARY KEY, 
Date DATE,
description TEXT,
category TEXT,
price REAL)""")


connect_to_db.commit()
connect_to_db.close()
