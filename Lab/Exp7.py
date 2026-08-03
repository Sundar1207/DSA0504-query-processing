import pandas as pd

# Sales Data
sales_data = {
    "Item": [
        "Laptop", "Laptop",
        "Mobile", "Mobile",
        "Tablet", "Tablet",
        "Printer", "Printer",
        "Monitor", "Monitor"
    ],
    "Salesperson": [
        "John", "Alice",
        "John", "Mary",
        "Alice", "David",
        "Mary", "John",
        "David", "Alice"
    ],
    "Sale_Value": [
        55000, 60000,
        25000, 27000,
        32000, 31000,
        15000, 18000,
        22000, 24000
    ]
}

# Create DataFrame
df = pd.DataFrame(sales_data)

print("Sales Data")
print(df)

# Create Pivot Table
pivot_table = pd.pivot_table(
    df,
    values="Sale_Value",
    index="Item",
    aggfunc=["max", "min"]
)

print("\nPivot Table (Maximum and Minimum Sale Value)")
print(pivot_table)