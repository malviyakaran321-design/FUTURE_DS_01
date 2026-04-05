import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Sample - Superstore.csv")

# Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Total Sales & Profit
print("Total Sales:", df['Sales'].sum())
print("Total Profit:", df['Profit'].sum())

# Sales by Category
category_sales = df.groupby('Category')['Sales'].sum()
print("\nSales by Category:\n", category_sales)

# Sales by Region
region_sales = df.groupby('Region')['Sales'].sum()
print("\nSales by Region:\n", region_sales)

# Top 10 Products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products:\n", top_products)

# Sales Trend
sales_trend = df.groupby('Order Date')['Sales'].sum()
sales_trend.plot()
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()

# Category Chart
category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.show()
