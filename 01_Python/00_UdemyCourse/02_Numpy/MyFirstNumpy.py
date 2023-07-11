# =============== Numpy Array ===============
# =============== Import Numpy array ===============
# =============== import numpy as np ===============
# myFirstArray = [[1,2,3][4,5,6][7,8,9]]
# arr = np.Array(myFirstArray)
# print (arr)

# =============== built in Function  ===============
import numpy as np
# Generate Random List
rand01 = np.arange(1,10)
print ("np.arange is ",rand01)

# Generate List　of one's that has a certain deminsions
rand02 = np.ones((2,4))
print ("np.ones is ",rand02)

# Generate List　of that has a certain space between the first and last number
rand03 = np.linspace(1,5,10)
print ("np.linspace is ",rand03)

# Generate 2-D array with ones on the diagonal and zeros elsewhere
rand04 = np.eye(4)
print ("np.eye is ",rand04)

# Generate a random number between a Standard Normal distribution
rand05 = np.random.randn(3,3)
print ("np.random.randn is ",rand05)

# Generate a random number between a normal number
# the minimum number (the first paramter will be inclusive)
rand06 = np.random.randint(0,5,1)
print ("np.random.randint is ",rand06)

# Use the reshape method from a given array
# Numpyのデータ型の属性でreshapeが存在する
rand07 = np.arange(25)
print ("np.arange is ",rand07)
rand07 = rand07.reshape(5,5)
print ("np.reshape is ",rand07)
arr01 = rand07.shape
print (arr01)



