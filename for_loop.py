# for loop in python
for i in range (5):
    print("Hello, World!")

# print 1 to 5
for i in range (1,6):
    print(i)

# print 1 to 10
for i in range (1,11):
    print(i)

# even no of 1 to 20
for i in range (1,21):
    if i%2==0:
        print(i)

# odd no of 1 to 15
for i in range (1,16):
    if i%2!=0:
        print(i)

# print table of 5
for i in range (1,11):
    print("5 x",i,"=",5*i)

#print character of a string
s = "Hello"
for i in s:
    print(i)

#sum of numbers from 1 to 5
sum = 0
for i in range (1,6):
    sum += i
print("Sum of numbers from 1 to 5 is:", sum)

#print list elements
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(i)