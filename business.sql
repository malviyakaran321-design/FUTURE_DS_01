-- Total Sales & Profit
SELECT SUM(Sales) AS Total_Sales, SUM(Profit) AS Total_Profit
FROM superstore;

-- Sales by Category
SELECT Category, SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Category
ORDER BY Total_Sales DESC;

-- Sales by Region
SELECT Region, SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC;

-- Top 10 Products
SELECT "Product Name", SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY "Product Name"
ORDER BY Total_Sales DESC
LIMIT 10;

-- Profit by Category
SELECT Category, SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Profit DESC;

-- Loss-Making Products
SELECT "Product Name", SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY "Product Name"
HAVING SUM(Profit) < 0;
