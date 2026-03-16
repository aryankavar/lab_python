#array slicing
import array
arr=array('i',[10,20,30,40,50])
print("Array elements are:")
print(arr)

print("Slicing from index 1 to 3:", arr[1:4])
print("Slicing from index 0 to 2:", arr[0:3])
print("Slicing from index 2 to end:", arr[2:])
print("Slicing from start to index 3:", arr[:4])
print("Slicing with step 2:", arr[::2])
print("Slicing with negative step:", arr[::-1])
