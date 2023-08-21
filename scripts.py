import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Conectar a la base de datos
conn = sqlite3.connect("Northwind.db")

# Consulta para calcular el ticket promedio por cliente
query = '''
    SELECT c.CustomerName, AVG(od.Quantity * p.Price) as AverageTicket
    FROM Customers c
    JOIN Orders o ON c.CustomerID = o.CustomerID
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    GROUP BY c.CustomerName
    ORDER BY AverageTicket DESC
'''

# Leer los datos en un DataFrame
average_ticket_data = pd.read_sql_query(query, conn)

# Crear un gráfico de barras para el ticket promedio por cliente
plt.figure(figsize=(10, 5))
plt.bar(average_ticket_data["CustomerName"], average_ticket_data["AverageTicket"])
plt.title("Average Ticket per Customer")
plt.xlabel("Customer")
plt.ylabel("Average Ticket")
plt.xticks(rotation=90)
plt.tight_layout()

# Mostrar el gráfico
plt.show()





