# 1. Create A data label that has a middle level label
# 2. Use the loc attribute to get a certain data
# 3. Use the xs function to get a certain data 

# 1. Create A data label that has a middle level label
# Index Levels

import pandas as pd
import numpy as np


outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
# Creates a list of tuples, with the pair of outside and inside
hier_index = list(zip(outside,inside))
print (hier_index)
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
print(df)
# 2. Use the loc attribute to get a certain data
print(df.loc["G1"].loc[1])
# 3. Use the xs function to get a certain data 
df.index.names = ['Group','Num']
print(df.xs(1, level='Num'))

