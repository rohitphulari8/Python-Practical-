Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import numpy as np
#check numpy version
print(np.__version__)
2.3.2
#creating empty array with numpy
arr1 = np.array([])
print(arr1)
[]

arr2 = np.array([1,2,3,4])
print(arr2)
[1 2 3 4]

# create a numpy array using tuple
arr3 = np.array((1,2,3,4))
print(arr3)
[1 2 3 4]

#checking type of array ele
type(arr3)
<class 'numpy.ndarray'>

#Creating 0-D array
arr = np.array(42)
print(arr)
42

#creating 1-D & 2-D array

array = np.array([1,2,3,4])
print(array)
[1 2 3 4]

array1 = np.array([[1,2,3,4],[5,6,7,8]])
print(array1)
[[1 2 3 4]
 [5 6 7 8]]

#creating 3-D array
array2 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[11,12,13]]])
print(array2)
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [11 12 13]]]
>>> 
>>> #Checking Dimensions the array have
>>> a = np.array(20)
>>> b = np.array([1,2])
>>> c = np.array([[1,2],[3,4]])
>>> d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
>>> print(a)
20
>>> print(b)
[1 2]
>>> #now check dimension by using ndim
>>> print(a.ndim)
0
>>> print(b.ndim)
1
>>> print(c.ndim)
2
>>> print(d.ndim)
3
>>> #ndim is an attribute that numpy provides to check array dimension
>>> 
>>> #Creating an array with 5 dimensions
>>> 
>>> ar = np.array([1,2,3,4],ndim=5)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    ar = np.array([1,2,3,4],ndim=5)
TypeError: array() got an unexpected keyword argument 'ndim'
>>> 
>>> ar = np.array([1,2,3,4],ndmin=5)
>>> print(ar)
[[[[[1 2 3 4]]]]]
>>> 
>>> 
>>> # Indexing
>>> 
>>> n = np.array([1,2,3,4,5])
>>> print(n)
[1 2 3 4 5]
>>> #print ele present at 0th index
>>> print(n[0])
1
>>> print(n[3]) #at 3rd index
4

