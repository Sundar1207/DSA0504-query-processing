import pandas as pd

# (Using the same DataFrame df from Question 8)
pivot_sales = pd.pivot_table(df, index=['Region', 'Manager', 'SalesMan'], values=['Sale_amt'], aggfunc='sum')
print(pivot_sales)
