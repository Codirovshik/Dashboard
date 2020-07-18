import sqlite3
import matplotlib.pyplot as plt

input_products_name = []
input_products_all_count = []
input_products_count_in_installments = []
input_products_count_no_in_installments = []

class DBClass:
    def __init__(self):
        self.nameTable = 'products'
        self.DB = sqlite3.connect('storage.db')
        self.DBconn = self.DB.cursor()
        self.DBconn.execute(f''' CREATE TABLE IF NOT EXISTS products(product_name text, count int, in_installments boolean); ''')
        self.DB.commit()
        self.DB.close()

    def addData(self, product_name, count, in_installments):
        param = [product_name, count, in_installments]
        self.DB = sqlite3.connect('storage.db')
        self.DBconn = self.DB.cursor()
        self.DBconn.execute(f"INSERT INTO products VALUES (?, ?, ?);", param)
        self.DB.commit()
        self.DB.close()
        
    
    def getDB(self):
        
        self.DB = sqlite3.connect('storage.db')
        self.DBconn = self.DB.cursor()
        
        for row in self.DBconn.execute(f"SELECT product_name FROM products;"):
            input_products_name.append(row)
        
        for row in self.DBconn.execute(f"SELECT count FROM products;"):
            input_products_all_count.append(row)


        for row in self.DBconn.execute(f"SELECT count FROM products WHERE in_installments='false';"):
            input_products_count_no_in_installments.append(row)

        for row in self.DBconn.execute(f"SELECT count FROM products WHERE in_installments='true';"):
            input_products_count_in_installments.append(row)
        
        self.DB.close()
         

output_products_name = []
output_products_all_count = []
output_products_count_in_installments = []
output_products_count_no_in_installments = []

def fillData():
    for i in input_products_name:
        output_products_name.append(i[0])

    for i in input_products_all_count:
        output_products_all_count.append(i[0])

    for i in input_products_count_no_in_installments:
        output_products_count_no_in_installments.append(i[0])

    for i in input_products_count_in_installments:
        output_products_count_in_installments.append(i[0])


