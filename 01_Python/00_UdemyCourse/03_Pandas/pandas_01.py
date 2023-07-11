import numpy as np
import pandas as pd

arr01 = np.arange(1,4)
lables = ['a','b','c']
dict01 = {'a':1,'b':2,'c':3}
# print dictionary with a certain key value 
print(dict01['a'])

# Create a Pandas Series that will label each value with each list
pd_arr = pd.Series(arr01)
print(pd_arr)

# Create a Pandas Series that will label each value with each lables and dict01
pd_arr02 = pd.Series(arr01,lables)
print(pd_arr02)

# Create a Pandas Series that will label each value with a dictionary
pd_arr03 = pd.Series(dict01)
print(pd_arr03)

# Select the second label for each pd_arr
print(pd_arr[1])
print(pd_arr02["b"])
print(pd_arr03["b"])


