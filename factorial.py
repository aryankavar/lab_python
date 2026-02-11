num = int(input("Enter a number: "))
Factorial = 1

if num < 0:
    print("Sorry factorial does not exist for negative numbers")
elif num == 1 or num == 0:
    print("The factorial of", num, "is 1")
else:
    for i in range(1, num + 1):
        Factorial = Factorial * i
    print("The factorial of", num, "is", Factorial)
    