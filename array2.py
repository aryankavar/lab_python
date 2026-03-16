#array indexing
from array import array
arr=array('i',[10,20,30,40,50])
print("Array elements are:")
print(arr)

print("Element at index 2:", arr[2])

print("Element at index 4:", arr[4])

print("Element at index 0:", arr[0])

#negative indexing
print("Element at index -1:", arr[-1])
print("Element at index -3:", arr[-3])
print("Element at index -5:", arr[-5])

#modifying array elements
arr[1] = 25
print("Array after modifying element at index 1:")
print(arr)
