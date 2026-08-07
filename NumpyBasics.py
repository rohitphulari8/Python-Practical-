Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> 
>>> h = np.array([1,2,3,5,76,8,565,)]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> 
>>> h = np.array([1,2,3,4,53,2,3123,])
>>> print(h)
[   1    2    3    4   53    2 3123]
>>> 
>>> #access any two ele using thier index position and add them
>>> 
>>> print(h[3]+h[2])
7
>>> 
>>> # accessing any row and column ele in 2-D array
>>> 
>>> n = np.array([[34,5,6],[1,2,3]])
>>> print(n)
[[34  5  6]
 [ 1  2  3]]
>>> print("2nd row and 1st col",n[1,0])
2nd row and 1st col 1
>>> print("2nd row and 2nd col: ",n[1,1])
2nd row and 2nd col:  2
>>> 
>>> 
>>> a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[11,12,13]]])
>>> print(a)
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [11 12 13]]]
>>> print(a[0,1,2])
6
>>> 
>>> 
>>> #Slicing of array [start:end] / [start:end:step]
>>> 
>>> b = np.array([1,2,3,4,5])
>>> #slice from 3 to 5
>>> print(3:5)
SyntaxError: invalid syntax
>>> print(b[3:5])
[4 5]
>>> print(b[1:3])
[2 3]
>>> 











# slice from index 2 to end
print(b[4::])
[5]
print(b[2::])
[3 4 5]

#slice from index 0 to 3 where 3 is not included
print(b[::3])
[1 4]
