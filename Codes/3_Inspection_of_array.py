''' a.shape - array dimension
    len(a) - lenght of an array
    b.ndim - number of array dimensions
    e.size - number of array elements
    b.dtype - datatype of array elements
    b.astype(int) - convert an array to an different type'''

import numpy as np

a = [[30,40,50], [40,30,50]]
arr = np.array(a)
print(arr)
print(arr.shape) # rows and colums
print(len(arr)) # number of nested values
print(np.size(arr)) # number of elements
print(type(arr)) # datatype of variable
print(arr.dtype) # datatype of array
print(arr.astype(float)) # conversion of datatype