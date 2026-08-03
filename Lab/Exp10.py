import pandas as pd
import numpy as np

# Create DataFrame with random values
np.random.seed(0)
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])

# Function to color code text
def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

# Apply styling
styled_df = df.style.applymap(color_negative_red)
styled_df
