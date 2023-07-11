# Create two tables and merge the two tables
# In one table and check what are the unique values 
# Create a csv file and import that to pandas

# Create two tables and merge the two tables

import pandas as pd 
import numpy as np

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
data2 = {
    'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
    'Person':['Kenji','Charlie','Miki','Vanessa','Carl','Sarah'],
}

df = pd.DataFrame()
