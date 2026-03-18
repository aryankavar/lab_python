def add(a, b):
    print("a =", a)
    print("b =", b)
    return a + b
result = add(3, 5)
print("sum =", result)

# student details
def student_details(name, age, grade):
    print("Name:", name)
    print("Age:", age)
    print("Grade:", grade)
student_details("Alice", 20, "A")

# simple interest
def calculate_simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    print("Simple Interest:", si)
calculate_simple_interest(1000, 5, 2)

# area of circle
def area_of_circle(radius):
    pi = 3.14159
    area = pi * radius ** 2
    print("Area of circle with radius", radius, "is:", area)
area_of_circle(5)
area_of_circle(1.5)

#check number is positive, negative or zero
def check_number(num):
    if num > 0:
        print(num, "is a positive number.")
    elif num < 0:
        print(num, "is a negative number.")
    else:
        print(num, "is zero.")
check_number(10)
check_number(-5)
check_number(0)

# odd or even
def is_odd(num):
    if num % 2 != 0:
        print(num, "is an odd number.")
    else:
        print(num, "is an even number.")
is_odd(7)
is_odd(10)

# arithmetic operations
def arithmetic_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Undefined (division by zero)"
    print("Addition:", addition)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)
    print("Division:", division)
arithmetic_operations(10, 5)
