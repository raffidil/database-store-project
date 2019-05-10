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


# IT NEEDS TO BE CHECKED
def warehouse_value(wid):
    db.execute(
        """select sum(Quantity)*Price 
        from Stock,Item 
        where Stock.Iid==Item.Id and Stock.Wid == ?""", (wid,))
    return db.fetchone()[0]


def all_warehouse_values():
    for row in db.execute("""select Stock.Wid, sum(Quantity)*Price from Stock,Item where Stock.Iid==Item.Id group by Stock.Wid"""):
        print(row)


def staff_info(id):
    db.execute("""select Staff.Id,Staff.Name,Warehouse.City from Staff,Warehouse where Staff.Id==Warehouse.Mid and Staff.Id== ?""", (id,))
    return db.fetchone()


def all_staff_info():
    for row in db.execute(
            """select Staff.Id,Staff.Name,Warehouse.City
             from Staff,Warehouse 
             where Staff.Id==Warehouse.Mid"""):
        print(row)


def total_quantity_of_each_city():
    for row in db.execute("""select city,sum(Quantity) from Stock, Warehouse where Stock.Wid==Warehouse.id group by city"""):
        print(row)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_command():
    cls()
    return input("""
    |  1. Insert Staff
    |  2. Insert Item
    |  3. Insert Warehouse
    |  4. Insert Stock
    ====================================
    |  5. Total Quantity
    ====================================
    |  6. Value of Warehouse by ID
    |  7. Total Value of All Warehouses
    ====================================
    |  8. Staff Info by Id
    |  9. All Staff Informations
    ====================================
    |  10. Total Quantity of All Cities
    ====================================
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
        print("Total Quantity of Stocks in All Warehouses: {}".format(
            str(total_quantity())))
        dummy = input("\nPress Enter to continue...")
    if _command == '6':
        cls()
        _warehouse_id = input("Input Warehouse ID: ")
        print("Total Value of Warehouse #{} : {}".format(
            str(_warehouse_id),
            str(warehouse_value(_warehouse_id))))
        dummy = input("\nPress Enter to continue...")
    if _command == '7':
        cls()
        print("Total Value of All Warehouses: ")
        all_warehouse_values()
        dummy = input("\nPress Enter to continue...")
    if _command == '8':
        cls()
        _staff_id = input("Input Staff ID: ")
        print("staff info: {}".format(str(staff_info(_staff_id))))
        dummy = input("\nPress Enter to continue...")
    if _command == '9':
        cls()
        print("All Staff info:\n")
        all_staff_info()
        dummy = input("\nPress Enter to continue...")
    if _command == '10':
        cls()
        print("Total Quantity of Each City:\n")
        total_quantity_of_each_city()
        dummy = input("\nPress Enter to continue...")

    _command = get_command()

# close connection
connection.commit()
connection.close()
