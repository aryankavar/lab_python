age = int(input("Enter your age: "))
if age < 18:
    print("You are not eligible to vote.")
else:
    print("You are eligible to vote.")

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

num = int(input("Enter a number to check positive, negative or zero: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

age = int(input("Enter your age to check eligibility for driving license: "))
if age >= 18:
    print("You are eligible for a driving license.")
else:
    print("You are not eligible for a driving license.")
