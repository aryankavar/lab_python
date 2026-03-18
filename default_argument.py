# square of number
def square(num=2):
    return num ** 2
print("Square of default number:", square())
print("Square of 5:", square(5))

# greet
def greet(name="Guest"):
    print("Hello,", name + "!")
greet()
greet("Alice")

# sum of two numbers
def add(a, b=5):
    print("sum =", a + b)
add(10)
add(10, 15)