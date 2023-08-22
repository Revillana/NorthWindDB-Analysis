# NorthWindDB-Analysis
Este código es un script que utiliza las bibliotecas SQLite, Pandas y Matplotlib en Python para realizar una serie de análisis y visualizaciones de datos relacionados con ventas y productos en una base de datos llamada "Northwind.db". A continuación, se explican cada una de las secciones del código y sus aplicaciones:

1. **Top 5 Most Selled Products (Productos más vendidos):** Este bloque realiza una consulta SQL para obtener los 5 productos más vendidos. Luego, crea un gráfico de barras con el nombre del producto en el eje X y las ventas en el eje Y. El gráfico se titula "Top 5 Most Selled Products".

2. **Most Used Supplier (Distribuidor más usado):** Aquí se obtiene el distribuidor que más productos ha suministrado. Se genera un gráfico de barras con el nombre del distribuidor en el eje X y la cantidad de productos en el eje Y. El gráfico se titula "Most Used Supplier".

3. **Most Profitable Supplier by Different Locations (Distribuidor más rentable según diferentes ubicaciones):** En este bloque se categorizan los ingresos de los distribuidores por ubicación geográfica y se crea un gráfico de barras que muestra los ingresos por ubicación. El gráfico se titula "Supplier Revenue by Geographic Zone".

4. **Employees Who Have Sold the Most in Each Category (Empleados que han vendido más de cada categoría):** Aquí se muestra un gráfico de barras que compara las ventas de los empleados en diferentes categorías de productos. Cada barra representa un empleado y su venta total en una categoría. El gráfico se titula "Sales by Category".

5. **Least Profitable Categories (Categorías menos rentables):** En este bloque se obtienen las categorías menos rentables en función del margen entre el precio y el costo de los productos. Se genera un gráfico de barras con el nombre de la categoría en el eje X y el margen en el eje Y. El gráfico se titula "Less Productive Category".

6. **5 Most Profitable Products (5 Productos más rentables):** Se obtienen los 5 productos más rentables y se crea un gráfico de barras con el nombre del producto en el eje X y el margen en el eje Y. El gráfico se titula "Top 5 More Profit Products".

7. **Monthly and Annual Sales per Product (Ventas mensuales y anuales por producto):** Se obtienen las ventas mensuales y anuales de cada producto y se crean dos gráficos de barras: uno para las ventas anuales y otro para las ventas mensuales.

8. **Top 5 Customers (5 Mejores Clientes):** Aquí se identifican los 5 mejores clientes en función del gasto total y se genera un gráfico de barras con el nombre del cliente en el eje X y el gasto en el eje Y.

9. **Employees with the Highest Monthly Sales (Empleados con más ventas al mes):** Se calculan las ventas mensuales de los empleados y se crean dos gráficos de barras: uno que muestra las ventas totales por empleado y otro que compara las ventas en diferentes meses.

10. **Average Ticket per Customer (Ticket medio por cliente):** Se calcula el ticket medio por cliente y se crea un gráfico de barras que muestra el promedio del ticket en el eje Y y el nombre del cliente en el eje X.

11. **Most Efficient Employees (Empleados más eficientes):** Se identifican los empleados más eficientes en función del número total de órdenes que han manejado. Se genera un gráfico de barras que muestra el número de órdenes en el eje Y y el nombre del empleado en el eje X.

Cada bloque del código realiza una consulta SQL para obtener los datos relevantes de la base de datos y luego utiliza Pandas y Matplotlib para visualizar y representar esos datos en forma de gráficos de barras. Cada gráfico está diseñado para proporcionar información visualmente atractiva y comprensible sobre diferentes aspectos de las ventas y los productos en la base de datos "Northwind.db".

This code is a script that uses the SQLite, Pandas, and Matplotlib libraries in Python to perform a series of data analysis and visualizations related to sales and products in a database called "Northwind.db." Below, each section of the code and its applications are explained:

1. **Top 5 Most Sold Products:** This section executes an SQL query to retrieve the top 5 best-selling products. It then creates a bar chart with the product name on the X-axis and sales on the Y-axis. The chart is titled "Top 5 Most Sold Products."

2. **Most Used Supplier:** In this section, the supplier that has supplied the most products is identified. A bar chart is generated with the supplier name on the X-axis and the quantity of products on the Y-axis. The chart is titled "Most Used Supplier."

3. **Most Profitable Supplier by Different Locations:** This section categorizes supplier revenues by geographical location and creates a bar chart illustrating revenues by location. The chart is titled "Supplier Revenue by Geographic Zone."

4. **Employees Who Have Sold the Most in Each Category:** This section presents a bar chart comparing employee sales in different product categories. Each bar represents an employee and their total sales in a category. The chart is titled "Sales by Category."

5. **Least Profitable Categories:** Here, the least profitable categories are identified based on the margin between the price and cost of products. A bar chart is generated with the category name on the X-axis and the margin on the Y-axis. The chart is titled "Less Productive Category."

6. **5 Most Profitable Products:** The top 5 most profitable products are obtained, and a bar chart is created with the product name on the X-axis and the margin on the Y-axis. The chart is titled "Top 5 More Profit Products."

7. **Monthly and Annual Sales per Product:** Monthly and annual sales for each product are obtained, and two bar charts are created: one for annual sales and another for monthly sales.

8. **Top 5 Customers:** In this section, the top 5 customers based on total spending are identified, and a bar chart is generated with the customer name on the X-axis and spending on the Y-axis.

9. **Employees with the Highest Monthly Sales:** Monthly sales for employees are calculated, and two bar charts are created: one displaying total sales per employee and another comparing sales in different months.

10. **Average Ticket per Customer:** The average ticket per customer is calculated, and a bar chart is generated showing the average ticket on the Y-axis and the customer name on the X-axis.

11. **Most Efficient Employees:** The most efficient employees based on the total number of orders they have handled are identified. A bar chart is generated showing the number of orders on the Y-axis and the employee name on the X-axis.

Each code section performs an SQL query to retrieve relevant data from the "Northwind.db" database. It then utilizes Pandas and Matplotlib to visualize and present this data as bar charts. Each chart is designed to provide visually appealing and comprehensible insights into different aspects of sales and products within the "Northwind.db" database.
