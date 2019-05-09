import sqlite3
import os
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
connection.commit()

# code


def insert_staff(id, name):
    db.execute(
        """INSERT INTO Staff (Id, Name) VALUES (?,?)""", (id, name))
    connection.commit()



def insert_item(id, name, price):
    db.execute(
        """INSERT INTO Item (Id, Name, Price) VALUES (?,?,?)""", (id, name, price))
    connection.commit()


def insert_warehouse(id, mid, city):
    db.execute(
        """INSERT INTO Warehouse (Id, Mid, City) VALUES (?,?,?)""", (id, mid, city))
    connection.commit()


def insert_stock(iid, wid, quantity):
    db.execute(
        """INSERT INTO Stock (Iid, Wid, Quantity) VALUES (?,?,?)""", (iid, wid, quantity))
    connection.commit()


def total_quantity():
    db.execute(
        """select sum(Quantity) from stock;""")
    return db.fetchone()[0]

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_command():
    cls()
    return input("""
    |  1.Insert Staff
    |  2.Insert Item
    |  3.Insert Warehouse
    |  4.Insert Stock
    |  5.Total Quantity
    |  0.exit\n
    #  command: """)


# main function


_command = get_command()
while _command is not '0':
    if _command == '1':
        cls()
        _staff_id = input("Input Staff ID: ")
        _staff_name = input("Input Staff Name: ")
        insert_staff(_staff_id, _staff_name)
        print("Staff Added!")
        dummy = input("\nPress Enter to continue...")
    if _command == '2':
        cls()
        _item_id = input("Input Item ID: ")
        _item_name = input("Input Item Name: ")
        _item_price = input("Input Item Price: ")
        insert_item(_item_id, _item_name, _item_price)
        print("Item Added!")
        dummy = input("\nPress Enter to continue...")
    if _command == '3':
        cls()
        _warehouse_id = input("Input Warehouse ID: ")
        _warehouse_mid = input("Input Warehouse Manager ID: ")
        _warehouse_city = input("Input Warehouse City: ")
        insert_warehouse(_warehouse_id, _warehouse_mid, _warehouse_city)
        print("Warehouse Added!")
        dummy = input("\nPress Enter to continue...")
    if _command == '4':
        cls()
        _stock_iid = input("Input Item ID: ")
        _stock_wid = input("Input Warehouse ID: ")
        _stock_qnty = input("Input Item Quantity: ")
        insert_stock(_stock_iid, _stock_wid, _stock_qnty)
        print("Stock Added!")
        dummy = input("\nPress Enter to continue...")
    if _command == '5':
        cls()
        print("\tTotal Quantity of Stocks in All Warehouses: {}".format(
            str(total_quantity())))

    _command = get_command()

# close connection
connection.commit()
connection.close()
