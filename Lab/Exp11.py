import pandas as pd
import numpy as np

np.random.seed(0)
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])

# Introduce NaN values
df.iloc[0, 1] = np.nan
df.iloc[3, 2] = np.nan
df.iloc[4, 0] = np.nan
df.iloc[9, 3] = np.nan

# Highlight NaN values
styled_df = df.style.highlight_null(null_color='yellow')
styled_df
