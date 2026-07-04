import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("sales_data (1).csv")

# Data Cleaning
df = df.drop_duplicates()
df = df.fillna(0)

# -------------------------
# Sales Analysis
# -------------------------

total_sales = df["Total_Sales"].sum()
best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

print(" SALES ANALYSIS REPORT")
print("-" * 40)
print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Best Selling Product: {best_product}")

# -------------------------
# Bar Chart
# -------------------------

product_sales = df.groupby("Product")["Total_Sales"].sum()

plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.close()

# -------------------------
# Line Chart
# -------------------------

daily_sales = df.groupby("Date")["Total_Sales"].sum()

plt.figure(figsize=(8,5))
daily_sales.plot(kind="line")
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("line_chart.png")
plt.close()

# -------------------------
# Pie Chart
# -------------------------

region_sales = df.groupby("Region")["Total_Sales"].sum()

plt.figure(figsize=(7,7))
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.tight_layout()
plt.savefig("pie_chart.png")
plt.close()

print("\n Charts Created Successfully!")
print("bar_chart.png")
print("line_chart.png")
print("pie_chart.png")
