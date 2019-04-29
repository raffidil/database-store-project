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


def insert_staff(id, name):
    db.execute(
        """INSERT INTO Staff (Id, Name) VALUES (?,?)""", (id, name))


def insert_item(id, name, price):
    db.execute(
        """INSERT INTO Item (Id, Name, Price) VALUES (?,?,?)""", (id, name, price))


def insert_warehouse(id, mid, city):
    db.execute(
        """INSERT INTO Warehouse (Id, Mid, City) VALUES (?,?,?)""", (id, mid, city))


def insert_stock(iid, wid, quantity):
    db.execute(
        """INSERT INTO Warehouse (Iid, Wid, Quantity) VALUES (?,?,?)""", (iid, wid, quantity))


def print_command():
    a = input("""
        1.Insert Staff
        2.Insert Item
        3.Insert Warehouse
        4.Insert Stock
        0.exit\n
        command: """)
    return a


# main function
_command = print_command()


while _command is not '0':
    if _command == '1':
        _staff_id = input("Input Staff ID: ")
        _staff_name = input("Input Staff Name: ")
        insert_staff(_staff_id, _staff_name)
    _command = print_command()


# close connection
connection.commit()
connection.close()
