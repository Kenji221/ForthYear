import numpy as np
import pandas as pd

# 1. Create a 3x3 DataFrame that has a non value
# 2. Use dropna to drop the whole column that has a non value
# 3. Use the thresh function
# 4. use the fillna value and fill a missing value with the mean

# 1. Create a 3x3 DataFrame that has a non value
df = pd.DataFrame({
    'A':[1,2,np.nan],
    'B':[1,2,np.nan],
    'C':[1,np.nan,np.nan]
})
print(df)
# 2. Use dropna to drop the whole column that has a non value
print(df.dropna())

# 3. Use the thresh function
print(df.dropna(thresh=1))

print(df['A'].fillna(value=df['A'].mean()))
