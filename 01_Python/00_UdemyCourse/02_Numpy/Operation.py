#  1. Add two arrays to each other 
#  2. Add a scalar to each arrays
#  3. devide two arrays to each other 
#  4. take the root of each element of the array 

#  1. Add two arrays to each other 
import numpy as np
arr1 = np.arange(1,11)

arr2 = arr1 + arr1
print(arr2)

#  2. Add a scalar to each arrays
arr1 = np.arange(1,11)
arr3 = arr1 + 100
print (arr3)

#  3. devide two arrays to each other 
arr1 = np.arange(1,11)
arr4 = arr1/arr1
print(arr4)

#  4. take the root of each element of the array 
arr1 = np.arange(1,11)
arr4 = np.sqrt(arr1)
print(arr4)


