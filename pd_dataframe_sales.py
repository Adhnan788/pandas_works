
sales = [
    {"order_id": 101, "product": "Laptop", "category": "Electronics", "region": "North", "year": 2022, "quantity": 5, "price": 75000, "revenue": 375000},
    {"order_id": 102, "product": "Mobile Phone", "category": "Electronics", "region": "South", "year": 2023, "quantity": 12, "price": 25000, "revenue": 300000},
    {"order_id": 103, "product": "Office Chair", "category": "Furniture", "region": "West", "year": 2021, "quantity": 20, "price": 6500, "revenue": 130000},
    {"order_id": 104, "product": "Desk", "category": "Furniture", "region": "East", "year": 2022, "quantity": 10, "price": 12000, "revenue": 120000},
    {"order_id": 105, "product": "Headphones", "category": "Accessories", "region": "North", "year": 2023, "quantity": 30, "price": 3000, "revenue": 90000},
    {"order_id": 106, "product": "Smart Watch", "category": "Electronics", "region": "South", "year": 2024, "quantity": 18, "price": 15000, "revenue": 270000},
    {"order_id": 107, "product": "Printer", "category": "Electronics", "region": "West", "year": 2021, "quantity": 7, "price": 22000, "revenue": 154000},
    {"order_id": 108, "product": "Tablet", "category": "Electronics", "region": "East", "year": 2022, "quantity": 14, "price": 32000, "revenue": 448000},
    {"order_id": 109, "product": "Bookshelf", "category": "Furniture", "region": "North", "year": 2023, "quantity": 9, "price": 9000, "revenue": 81000},
    {"order_id": 110, "product": "Keyboard", "category": "Accessories", "region": "South", "year": 2024, "quantity": 40, "price": 2500, "revenue": 100000},
    {"order_id": 111, "product": "Mouse", "category": "Accessories", "region": "West", "year": 2022, "quantity": 50, "price": 1200, "revenue": 60000},
    {"order_id": 112, "product": "Monitor", "category": "Electronics", "region": "East", "year": 2021, "quantity": 11, "price": 18000, "revenue": 198000},
    {"order_id": 113, "product": "Air Conditioner", "category": "Appliances", "region": "North", "year": 2023, "quantity": 6, "price": 42000, "revenue": 252000},
    {"order_id": 114, "product": "Refrigerator", "category": "Appliances", "region": "South", "year": 2022, "quantity": 4, "price": 55000, "revenue": 220000},
    {"order_id": 115, "product": "Washing Machine", "category": "Appliances", "region": "West", "year": 2024, "quantity": 5, "price": 38000, "revenue": 190000},
    {"order_id": 116, "product": "Router", "category": "Electronics", "region": "East", "year": 2023, "quantity": 22, "price": 4500, "revenue": 99000},
    {"order_id": 117, "product": "Power Bank", "category": "Accessories", "region": "North", "year": 2021, "quantity": 35, "price": 2000, "revenue": 70000},
    {"order_id": 118, "product": "Projector", "category": "Electronics", "region": "South", "year": 2022, "quantity": 3, "price": 65000, "revenue": 195000},
    {"order_id": 119, "product": "Conference Table", "category": "Furniture", "region": "West", "year": 2023, "quantity": 2, "price": 85000, "revenue": 170000},
    {"order_id": 120, "product": "USB Drive", "category": "Accessories", "region": "East", "year": 2024, "quantity": 60, "price": 900, "revenue": 54000}
]
import pandas as pd

df=pd.DataFrame(sales)
print(df)

print(df.shape)
print(df.columns)

print(df.head())
print(df.tail())

print(df.info())

#revenue analysis
total_revenue = df["revenue"].sum()
print("Total Revenue:", total_revenue)

max_revenue = df["revenue"].max()
print("max Revenue:", max_revenue)

min_revenue=df["revenue"].min()
print("min revenue",min_revenue)

total_quantity = df["quantity"].sum()
print("Total Quantity Sold:", total_quantity)