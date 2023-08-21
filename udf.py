import sqlite3
import pandas as pd

square = lambda n: n*n

#conn = sqlite3.connect("Northwind.db") metodo 1 se debe abrir y cerrar la conexion a bbdd
#conn.create_function("square",1,square)
#cursor = conn.cursor()
#cursor.execute ('''
#    SELECT * FROM Products
#    ''')
#results = cursor.fetchall()
#results_df = pd.DataFrame(results)
#conn.commit() 
#cursor.close()
#conn.close()
#print(results_df)

with sqlite3.connect("Northwind.db") as conn:
     conn.create_function("square", 1, square)
     cursor = conn.cursor()
     cursor.execute('SELECT *,square (Price) FROM Products WHERE Price > 0')
     results = cursor.fetchall()
     results_df= pd.DataFrame(results)
print(results_df)