# print no from 1 to 5
print("-----------Print numbers from 1 to 5:-----------")
i = 1
while i <= 5:
    print(i)
    i += 1

# sum of numbers take user input
print("-----------Sum of numbers from 1 to n:-----------")
n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Sum of numbers from 1 to", n, "is:", sum)    

# print odd no from 1 to 20
print("-----------Odd numbers between 1 and 20:-----------")
i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1

# print table of 4
print("-----------Table of 4:-----------")
i = 1
while i <= 10:
    print("4 x", i, "=", 4 * i)
    i += 1

# print revers number 
print("-----------Print reverse number:-----------")
i = int(input("Enter a number: "))
while i > 0:
    print(i)
    i -= 1

#find largest number in list
print("-----------Finding largest number in the list:-----------")
my_list = [30, 53, 257, 82, 196]
i = 0
largest = my_list[0]
while i < len(my_list):
    if my_list[i] > largest:
        largest = my_list[i]
    i += 1
print("Largest number in the list is:", largest)

#print even number between 1 and 20
print("-----------Even numbers between 1 and 20:-----------")
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# largest number in list
print("-----------Finding largest number in the list:-----------")
my_list = [30, 53, 257, 82, 196]
largest = max(my_list)
print("Largest number in the list is:", largest)