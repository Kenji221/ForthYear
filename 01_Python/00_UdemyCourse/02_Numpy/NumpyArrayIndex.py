import numpy as np

# Index a certain range of the array
num01 = np.arange(1,5) 
num02 = num01[0:3]
num03 = num01[:3]
num04 = num01[3:]

print (num02)
print (num03)
print (num04)

# Changing Parameters
num11 = np.arange(0,20)

# BroadCast first 5 elements to 999
num11[:5] = 999

# BroadCast first 5 elements to 999
num12 = np.arange(0,10)
print("num 12 is ",num12)
num13 = num12[:5]
num13[:] = 888
print("num 13 is ",num13)
print("num 12 updated is ", num12)

# Indexing, two deminsional arrays
num14 = np.arange(5,46,5)
num15 = num14.reshape(3,3)

# print second row, second column
print(num15[2][1])
print(num15[2,1])

# Boolean Notation for array
num16 = np.arange(1,11)
bool_arr = num16 > 5 
print (bool_arr)
bool_arr[:]
print(bool_arr[bool_arr])

num17 = np.arange(1,11) 
print(num17[num17>5])