import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("Northwind.db")
#1.Productos mas vendidos
#2.Distribuidor mas usado
#3.Segun diferentes ubicaciones, distribuidor mas rentable
#4.Empleados que han vendido mas de cada categoria 
#5.Categorias menos rentables
#6.Productos mas rentables
#7.Categorias que reparten cada Shipper
#8.Ventas mensuales y anuales por porducto, categoria y empleado
#9.Mejores clientes
#10.Media de ventas en el año
#11.Productos más y menos vendidos en cada estacion del año (intervalos de fechas)
#12.Empleados con mas y menos ventas en cada mes o cada estacion del año (intervalo)
#13.Ticket medio (cantidad de productos) por cada empleado

# 3. Distribuidor más rentable según diferentes ubicaciones
# 3. Cantidad de productos distribuidos por diferentes ubicaciones
query = '''
    SELECT CASE
               WHEN Country IN ('USA', 'Brazil', 'Canada') THEN 'Latinoamérica/EEUU'
               WHEN Country IN ('UK', 'Spain', 'Sweden', 'Germany', 'Italy', 'Norway', 'France', 'Denmark', 'Netherlands', 'Finland') THEN 'Europa'
               WHEN Country IN ('Japan', 'Australia', 'Singapore') THEN 'Asia'
               ELSE 'Otro'
           END AS Location,
           SupplierName,
           COUNT(DISTINCT p.ProductID) as ProductCount
    FROM Suppliers s
    JOIN Products p ON s.SupplierID = p.SupplierID
    GROUP BY Location, s.SupplierID
    ORDER BY Location, ProductCount DESC
'''

location_product_count = pd.read_sql_query(query, conn)

pivot_table = location_product_count.pivot_table(index='Location', columns='SupplierName', values='ProductCount', aggfunc='sum', fill_value=0)

pivot_table.plot(kind='bar', figsize=(10, 5))
plt.title("Cantidad de Productos Distribuidos por Ubicación y Proveedor")
plt.xlabel("Ubicación")
plt.ylabel("Cantidad de Productos")
plt.xticks(rotation=0)
plt.legend(title='Proveedor', loc='upper left', bbox_to_anchor=(1, 1))
plt.show()