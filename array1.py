#Array operation
from array import array

arr=array('i',[10,20,30,40,50])
print("Array elements are:")
print(arr)

arr.append(60)
print("Array after appending 60:")
print(arr)

insert_index = 2
arr.insert(insert_index, 25)
print("Array after inserting 25 at index 2:")
print(arr)

remove_index = 4
arr.pop(remove_index)
print("Array after removing element at index 4:")
print(arr)

x=arr.pop(3)
print("Array after popping element at index 3:")
print(arr)
print("Popped element:", x)

arr=array('i',[10,20,30,40,50])
print(arr.index(30))

print(arr.count(20))

arr.reverse()
print(arr)