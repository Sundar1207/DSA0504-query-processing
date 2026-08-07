import pandas as pd

# Sample DataFrame
data = {'Language': ['Python Programming', 'JavaScript', 'C++ Language', 'Data Science with Python']}
df = pd.DataFrame(data)

# Substring to find
substring = 'Python'

# Find index of substring
df['Substring_Index'] = df['Language'].str.find(substring)

print("DataFrame with Substring Index:")
print(df)
