import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("Northwind.db")

#1. Top 5 Most Selled Products// Productos más vendidos
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
plt.xlabel("Products")
plt.ylabel("Sales")
plt.xticks(rotation= 90)
plt.show()

############################################################################################################################################

#2. Most used supplier // Distribuidor mas usado
query = '''
    SELECT SupplierName, COUNT(p.ProductID) as Products
    FROM Suppliers s
    JOIN Products p ON s.SupplierID = p.SupplierID
    GROUP BY SupplierName
    ORDER BY Products DESC
'''
    
top_suppliers = pd.read_sql_query(query,conn)
top_suppliers.plot(x="SupplierName", y="Products",kind="bar",figsize=(10,5),legend=False)
plt.title("Most Used Supplier")
plt.xlabel("Supplier")
plt.ylabel("Products")
plt.xticks(rotation= 90)
plt.show()

############################################################################################################################################

# 3. Most profitable supplier by different locations // Distribuidor más rentable según diferentes ubicaciones
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

############################################################################################################################################

#4. Employees who have sold the most in each category // Empleados que han vendido más de cada categoria

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
plt.ylabel("Sales") 
plt.xticks(rotation = 30)
plt.legend(title='Employee', loc='upper left', bbox_to_anchor=(1,1))

plt.show()

##################################################################################################################################################

#5. Least profitable categories // Categorías menos rentables

query = '''
SELECT p.ProductName as Product, c.CategoryName as Category, p.Price - p.BCost as Margin
FROM Products p
JOIN Categories c ON p.CategoryID = c.CategoryID
GROUP BY Category
ORDER BY Margin ASC
'''
    
less_profit = pd.read_sql_query(query,conn)
less_profit.plot(x="Category", y="Margin",kind="bar",figsize=(10,5),legend=False)
plt.title("Less Productive Category")
plt.xlabel("Category")
plt.ylabel("Margin")
plt.xticks(rotation= 90)
plt.show()

####################################################################################################################################################

##################################################################################################################################################

#6. 5 Most profitable products // 5 Productos más rentables
query = '''
SELECT p.ProductName as Product, p.Price - p.BCost as Margin
FROM Products p
ORDER BY Margin DESC
LIMIT 5
'''  
more_profit = pd.read_sql_query(query,conn)
more_profit.plot(x="Product", y="Margin",kind="bar",figsize=(10,5),legend=False)
plt.title("Top 5 More Profit Products")
plt.xlabel("Product")
plt.ylabel("Margin")
plt.xticks(rotation= 90)
plt.show()

####################################################################################################################################################

##################################################################################################################################################

#7. Monthly and Annual Sales per Product // Ventas Mensuales y Anuales por Producto

query = '''
SELECT
    strftime('%Y', OrderDate) AS Year,
    strftime('%m-%Y', OrderDate) AS Month,
    p.ProductName AS Product_Name,
    SUM(od.Quantity) AS Product_Sales
FROM
    Products p
JOIN
    OrderDetails od ON p.ProductID = od.ProductID
JOIN
    Orders o ON od.OrderID = o.OrderID
GROUP BY
    Year, Month, Product_Name
ORDER BY
    Year, Month, Product_Name;
'''
sales_data = pd.read_sql_query(query, conn)
p_sales_data_year = sales_data.pivot_table(index='Year', columns='Product_Name', values='Product_Sales', fill_value=0)
p_sales_data_month = sales_data.pivot_table(index='Month', columns='Product_Name', values='Product_Sales', fill_value=0)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

p_sales_data_year.plot(kind='bar', ax=ax1)
ax1.set_title("Yearly Sales")
ax1.set_xlabel("Year")
ax1.set_ylabel("Sales")
ax1.legend(title='Product', loc='upper left', bbox_to_anchor=(1, 1))
ax1.tick_params(axis='x', rotation=45)

p_sales_data_month.plot(kind='bar', ax=ax2)
ax2.set_title("Monthly Sales")
ax2.set_xlabel("Month")
ax2.set_ylabel("Sales")
####################################################################################################################################################

##################################################################################################################################################

#8. Top 5 Customers// 5 Mejores Clientes
query = '''
SELECT c.CustomerName, SUM(od.Quantity * p.Price) as Total_Spent
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
GROUP BY c.CustomerName
ORDER BY Total_Spent DESC
LIMIT 5
'''
    
Customer_spent = pd.read_sql_query(query,conn)
Customer_spent.plot(x="CustomerName", y="Total_Spent",kind="bar",figsize=(10,5),legend=False)
plt.title("Top 5 Customer")
plt.xlabel("Customer")
plt.ylabel("Spent")
plt.xticks(rotation= 90)
plt.show()

####################################################################################################################################################

##################################################################################################################################################

#9. Employees with the highest monthly sales // Empleados con mas ventas al mes 
query = '''
SELECT e.LastName || ' ' || e.FirstName AS Employee,
       SUM(od.Quantity * p.Price) AS Total_Sale,
       strftime('%m-%Y', o.OrderDate) AS Month
FROM Employees e
JOIN Orders o ON e.EmployeeID = o.EmployeeID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
GROUP BY e.EmployeeID, e.LastName, e.FirstName, Month
ORDER BY Month, Total_Sale DESC;
'''
Sales_date = pd.read_sql_query(query, conn)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
ax1 = axes[0]
Sales_date.plot(x="Employee", y="Total_Sale", kind="bar", ax=ax1)
ax1.set_title("Total de Ventas por Empleado")
ax1.set_xlabel("Empleado")
ax1.set_ylabel("Total de Ventas")
ax1.set_xticklabels(Sales_date["Employee"], rotation=90)
ax1.legend().set_visible(False)
ax2 = axes[1]
pivot_table = Sales_date.pivot_table(index="Month", columns="Employee", values="Total_Sale")
selected_months = pivot_table.index[::3]  
pivot_table.loc[selected_months].plot(ax=ax2)
plt.tight_layout()
plt.show()

####################################################################################################################################################

##################################################################################################################################################

#10. Average Ticket per Customer // Ticket Medio por Cliente

query = '''
    SELECT c.CustomerName, AVG(od.Quantity * p.Price) as AverageTicket
    FROM Customers c
    JOIN Orders o ON c.CustomerID = o.CustomerID
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    GROUP BY c.CustomerName
    ORDER BY AverageTicket DESC
'''

average_ticket_data = pd.read_sql_query(query, conn)
plt.figure(figsize=(10, 5))
plt.bar(average_ticket_data["CustomerName"], average_ticket_data["AverageTicket"])
plt.title("Average Ticket per Customer")
plt.xlabel("Customer")
plt.ylabel("Average Ticket")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

####################################################################################################################################################

#11. Most Efficient Employees // Empleados Más Eficientes
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

plt.title("Most efficient Employees")
plt.xlabel("Employees")
plt.ylabel("Sales") 
plt.xticks(rotation = 45)

plt.show()
####################################################################################################################################################
