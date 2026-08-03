import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("alphabet_stock_data.csv")

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Select data between two specific dates
start_date = "2023-01-03"
end_date = "2023-01-09"

filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

# Display filtered data
print(filtered_df)

# Create Scatter Plot
plt.figure(figsize=(8,5))

plt.scatter(
    filtered_df["Volume"],
    filtered_df["Close"],
    color="blue",
    marker="o"
)

plt.title("Alphabet Inc. Stock Price vs Trading Volume")
plt.xlabel("Trading Volume")
plt.ylabel("Closing Stock Price")
plt.grid(True)

plt.show()