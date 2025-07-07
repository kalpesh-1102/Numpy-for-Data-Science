import numpy as np

arr = np.array([20,30,40,50])
# print(arr)
# print(type(arr)) # to check the type of an element in an array 

# slicing of an array
print(arr[0:2])

# slicing multidimentional arrays
a1 = np.array([[20,30,40,50],[60,70,80,90]])
# print(a1[0:2,0:2])
# print(a1[0:2,0:3]) # this will give me equal colums of each array, i.e 3 columns of both the array

# getting values of particular array 
print(a1[0,0:3]) # this will give me the elements of the first arry and if we put 1 in place of 0 i.e index 1, it will give elements of second array


# attribute of array
# print(np.shape(a1)) # this will give the shape of the array i.e 2 rows and 4 colums
# print(np.size(a1)) # gives total elements in the array, here 8
# print(np.ndim(a1)) # no of dimension 
# print(a1.dtype) # shows the datatype of the array, here int32

# print(a1.shape)
# print(len(arr))
# print(type(a1)) # datatype of variable 