import sqlite3

# create connection
connection = sqlite3.connect('database.db')
db = connection.cursor()

# initialize:
db.execute(
    """CREATE TABLE IF NOT EXISTS Item (Id number PRIMARY KEY, Name text, Price number)""")
db.execute(
    """CREATE TABLE IF NOT EXISTS Staff (Id number PRIMARY KEY, Name text)""")
db.execute(
    """CREATE TABLE IF NOT EXISTS Warehouse (Id number PRIMARY KEY, Mid number, City text)""")
db.execute(
    """CREATE TABLE IF NOT EXISTS Stock (Iid number ,Wid number, Quantity number)""")

# code


# close connection
connection.commit()
connection.close()
