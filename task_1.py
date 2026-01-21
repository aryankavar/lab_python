# calculate simple interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest,"\n")


# print numbers from 1 to 5
for i in range(1, 6):
    print(i)


# maximum of two numbers
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("The maximum number is:", num1)
else:
    print("The maximum number is:", num2)


# find the length of a string
input_string = input("\nEnter a string: ")
length = len(input_string)
print("The length of the string is:", length)


print("\nHello, World!")


# print 1st character of a string
string_input = input("\nEnter a string: ")
first_character = string_input[0]
print("The first character of the string is:", first_character)


# print last character of a string
string_input = input("\nEnter a string: ")
last_character = string_input[-1]
print("The last character of the string is:", last_character)


# check positive or negative number
number = int(input("\nEnter a number: "))

if number >= 0:
    print(number, "is a positive number.")
else:
    print(number, "is a negative number.")


# add three numbers
num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

sum_of_numbers = num1 + num2 + num3
print("The sum of the three numbers is:", sum_of_numbers)


# take input from user and make a task
name = input("\nEnter the task name: ")
deadline = input("Enter the deadline (YYYY-MM-DD): ")

print("Task", name, "has been set with a deadline of", deadline + ".")