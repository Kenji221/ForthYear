# 1: make a comparison with each column value with a certain number
# 2: Grab a column from the comparison you made in #1
# 3: Make a comarison using the & , |
# 4: use the reset_index 
# 5: make a list using the .spilt() function
# 6: add a column
# 7: add a row 

import numpy as np
import pandas as pd
from numpy.random import randn

# 5: make a list using the .spilt() function
newList_01 = 'A B C D E'.split()
newList_02 = 'F G H I J'.split()

# 1: make a comparison with each column value with a certain number
df_01 = pd.DataFrame(randn(5,5),[newList_01],[newList_02])
print(df_01)  

# 2: Grab a column from the comparison you made in #1
df_02=df_01[df_01['F']>0]
print(df_02)

# 3: Make a comarison using the & , |
df_03=df_01[(df_01['G']>-0.5) & (df_01['H'] > -0.5)]
print(df_03)

# 4: use the reset_index 
df_04 = df_01.reset_index()
print(df_04)

# 6: add a column
df_01['new']=newList_01
print(df_01)

df_05 = df_01.set_index('new',inplace = True)
print(df_05)