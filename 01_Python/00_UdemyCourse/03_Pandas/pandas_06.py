import pandas as pd
import numpy as np

# make a variable that has a three by three column with certain variables
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
print("The data frame is ",df)

# Create a new variable that will take in the dataframe and output a specific column
df_02 = df.groupby('Company')
print("each value of the companies are ",df_02)
# this will be the data object 

# Get the min value of the column
df_03 = df.groupby('Company').min()
print ("each minimum value of the companies are",df_03)


# Get the whole value of each column
df_04 = df.groupby('Company').describe()
print(df_04)


