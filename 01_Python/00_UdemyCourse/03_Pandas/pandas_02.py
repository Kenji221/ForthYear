import numpy as np
import pandas as pd
from numpy.random import randn


# Creating a table from a certain data frame
df = pd.DataFrame(randn(4,4),['a','b','c','d'],['e','f','g','h'])
print (df)
print (randn(3,3))

# Selecting a certain column
print(df['e'])

# Adding a certain column
df['new'] =df['e'] + df['f']
print (df)

# Dropping column 
df.drop('g',axis=1,inplace = True)
print (df)

# Selecting Columns through loc / iloc
# be careful that it starts with []
df_03 = df.loc['b']
df_04 = df.iloc[1]

print(df_03, df_04)


# Selecting Columns and rows 
df_05 = df.loc['b','e']
print (df_05)
