import pandas as pd
import numpy as np

np.random.seed(0)
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])

# Custom function to set background and text color across all cells
def custom_style(val):
    return 'background-color: black; color: yellow'

styled_df = df.style.applymap(custom_style)
styled_df
