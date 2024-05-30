import sqlite3
import time
import os

conn = sqlite3.connect("TechStoreStockInformation.db")

cursor = conn.cursor()
def loading():
    cls()
    time.sleep(0.25)
    print("Loading")
    time.sleep(0.25)
    cls()
    print("Loading.")
    time.sleep(0.25)
    cls()
    print("Loading..")
    time.sleep(0.25)
    cls()
    print("Loading...")
    time.sleep(0.25)
    cls()
    print("Done!")
    time.sleep(0.5)
    cls()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def user_menu():
    print()
    print("Get all product information - 1")
    print("Get all product information, sort by retail price ascending - 2")
    print("Get all product information, sort by retail price descending - 3")
    print("Get all product information, sort by manufacturing cost ascending - 4")
    print("Get all product information, sort by manufacturing cost descending - 5")


def get_all_stock_information():
    loading()
    cursor.execute('SELECT * FROM TechStoreStockInformation')
    TechStoreStockInformation = cursor.fetchall()

    for product in TechStoreStockInformation:
        print(f"{product[0]}. {product[1]}:")
        print(f"    Retail Price - ${product[2]}")
        print(f"    Manufacturing Price - ${product[3]}")
        print(f"    Weight - {product[4]} grams")
        print(f"    Stock - {product[5]} units")

def get_all_stock_information_by_ascending_retail_price():
    loading()
    query = "SELECT * FROM TechStoreStockInformation ORDER BY RetailPrice ASC"
    cursor.execute(query)
    get_all_stock_information_by_ascending_retail_price = cursor.fetchall()

    for index, product in enumerate(get_all_stock_information_by_ascending_retail_price):
        print(f"{product[0]}. {product[1]}:")
        print(f"    Retail Price - ${product[2]}")
        print(f"    Manufacturing Price - ${product[3]}")
        print(f"    Weight - {product[4]} grams")
        print(f"    Stock - {product[5]} units")

def get_all_stock_information_by_descending_retail_price():
    loading()
    query = "SELECT * FROM TechStoreStockInformation ORDER BY RetailPrice DESC"
    cursor.execute(query)
    get_all_stock_information_by_descending_retail_price = cursor.fetchall()

    for index, product in enumerate(get_all_stock_information_by_descending_retail_price):
        print(f"{product[0]}. {product[1]}:")
        print(f"    Retail Price - ${product[2]}")
        print(f"    Manufacturing Price - ${product[3]}")
        print(f"    Weight - {product[4]} grams")
        print(f"    Stock - {product[5]} units")

def get_all_stock_information_by_ascending_manufacturing_cost():
    loading()
    query = "SELECT * FROM TechStoreStockInformation ORDER BY ManufacturingCost ASC"
    cursor.execute(query)
    get_all_stock_information_by_ascending_manufacturing_cost = cursor.fetchall()

    for index, product in enumerate(get_all_stock_information_by_ascending_manufacturing_cost):
        print(f"{product[0]}. {product[1]}:")
        print(f"    Retail Price - ${product[2]}")
        print(f"    Manufacturing Price - ${product[3]}")
        print(f"    Weight - {product[4]} grams")
        print(f"    Stock - {product[5]} units")

def get_all_stock_information_by_descending_manufacturing_cost():
    loading()
    query = "SELECT * FROM TechStoreStockInformation ORDER BY ManufacturingCost DESC"
    cursor.execute(query)
    get_all_stock_information_by_descending_manufacturing_cost = cursor.fetchall()

    for index, product in enumerate(get_all_stock_information_by_descending_manufacturing_cost):
        print(f"{product[0]}. {product[1]}:")
        print(f"    Retail Price - ${product[2]}")
        print(f"    Manufacturing Price - ${product[3]}")
        print(f"    Weight - {product[4]} grams")
        print(f"    Stock - {product[5]} units")
while True:
    while True:
        cls()
        user_menu()
        print("What do you want to do?")
        user_input = input("> ")
        if user_input == "1":
            get_all_stock_information()
            break
        if user_input == "2":
            get_all_stock_information_by_ascending_retail_price()
            break
        if user_input == "3":
            get_all_stock_information_by_descending_retail_price()
            break
        if user_input == "4":
            get_all_stock_information_by_ascending_manufacturing_cost()
            break
        if user_input == "5":
            get_all_stock_information_by_descending_manufacturing_cost()
            break
        else:
            print("Error, please type a number.")
            time.sleep(3)

    print("Press enter to run another query")
    user_confirmation = input("> ")
    loading()
    