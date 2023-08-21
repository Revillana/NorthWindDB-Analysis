import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("Northwind.db")

#1. Productos más vendidos
query = '''
    SELECT p.ProductName, SUM(od.Quantity) as Sales
    FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY p.ProductName
    ORDER BY Sales DESC
    LIMIT 5
'''
    
top_products = pd.read_sql_query(query,conn)
top_products.plot(x="ProductName", y="Sales",kind="bar",figsize=(10,5),legend=False)
plt.title("Top 5 Most Selled Products")
plt.xlabel("Productos")
plt.ylabel("Sales")
plt.xticks(rotation= 90)
plt.show()

#2.Distribuidor mas usado
query = '''
    SELECT SupplierName, COUNT(p.ProductID) as Products
    FROM Suppliers s
    JOIN Products p ON s.SupplierID = p.SupplierID
    GROUP BY SupplierName
    ORDER BY Products DESC
'''
    
top_suppliers = pd.read_sql_query(query,conn)
top_suppliers.plot(x="SupplierName", y="Products",kind="bar",figsize=(10,5),legend=False)
plt.title("Distribuidor más usado")
plt.xlabel("Supplier")
plt.ylabel("Products")
plt.xticks(rotation= 90)
plt.show()

# 3.Distribuidor más rentable según diferentes ubicaciones
query = '''
    SELECT CASE
        WHEN Country IN ('USA','Brazil','Canada') THEN 'Latam/EEUU-Canada'
        WHEN Country IN ('UK','Spain', 'Sweden', 'Germany', 'Italy', 'Norway', 'France', 'Denmark', 'Netherlands', 'Finland') THEN 'Europe'
        WHEN Country IN ('Japan','Australia', 'Singapore') THEN 'Asia'
        ELSE 'Otro'
      END AS Location,
      SupplierName,
      SUM(Price*Quantity) as Revenue
      FROM OrderDetails od
      JOIN Products p ON p.ProductID = od.ProductID
      JOIN Suppliers s ON s.SupplierID = p.SupplierID
      GROUP BY Location, s.SupplierID
      ORDER BY Location, Revenue DESC
'''
location_revenue = pd.read_sql_query(query, conn)
pivot_table= location_revenue.pivot_table(index='Location', columns= 'SupplierName', values='Revenue', aggfunc='sum', fill_value= None)
pivot_table.plot(kind='bar', figsize=(10, 5))
plt.title("Supplier Revenue by Geographic Zone")
plt.xlabel("Geographic Zone")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.legend(title='Supplier', loc='upper left', bbox_to_anchor=(1,1))
plt.show()

#4.Empleados que han vendido más de cada categoria

query='''
SELECT c.CategoryName, e.FirstName || ' ' || e.LastName as Employee,
       SUM(od.Quantity) as Sales
FROM employees e
JOIN orders o ON e.EmployeeID = o.EmployeeID
JOIN orderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
JOIN categories c ON p.CategoryID = c.CategoryID
GROUP BY c.CategoryName, e.EmployeeID
ORDER BY Sales DESC, CategoryName DESC
'''
employees_categories = pd.read_sql_query(query, conn)
employees_categories2 = employees_categories.pivot_table(index='CategoryName', columns= 'Employee', values= 'Sales',aggfunc='sum', fill_value=0)
employees_categories2.plot(kind="bar",figsize=(10,5))

plt.title("Sales by Category")
plt.xlabel("Employee")
plt.ylabel("Category") 
plt.xticks(rotation = 90)
plt.legend(title='Sales', loc='upper left', bbox_to_anchor=(1,1))

plt.show()


#11. Empleados más eficientes
query = '''
    SELECT FirstName || " " || LastName as Employee, COUNT(*) as Total
    FROM Orders o
    JOIN Employees e ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total DESC
    LIMIT 10
'''
top_employees = pd.read_sql_query (query,conn)
top_employees.plot(x="Employee",y="Total", kind="bar",figsize=(10,5),legend=False)

plt.title("10 empleados más efectivos")
plt.xlabel("Empleados")
plt.ylabel("Total vendido") 
plt.xticks(rotation = 45)

plt.show()

