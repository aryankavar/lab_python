print("Welcome to Assignment 1!")

print("\nRajesh Kumar\nFlat No. 101, Sunshine Apartments\nMG Road, Sector 15\nRajkot, Pincode:360004 India.")

x=150
y=120.50

print("\nsum of",x,"and",y,"is:",x+y)
print("subtraction of",x,"and",y,"is:",x-y)
print("multiplication of",x,"and",y,"is:",x*y)
print("division of",x,"and",y,"is:",x/y)


radius = int(input("\nEnter the radius of the circle: "))
area = 3.14 * radius * radius
print("Area of the circle with radius",radius,"is:",area)
print("Circumference of the circle with radius",radius,"is:",2*3.14*radius)

print("\nSimple Interest Calculation")
principal = int(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = int(input("Enter the time in years: "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest is:",simple_interest)

print("\nPerameter of Rectangle Calculation")
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the breadth of the rectangle: "))
perimeter = 2 * (length + width)
print("Perameter of the rectangle is:",perimeter)

print("\nPerameter and Area of Rectangle Calculation")
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the breadth of the rectangle: "))
perimeter = 2 * (length + width)
area = length * width
print("Perameter of the rectangle is:",perimeter)
print("Area of the rectangle is:",area)

print("\nPerimeter of Triangle Calculation")
side1 = int(input("Enter the first side of the triangle: "))
side2 = int(input("Enter the second side of the triangle: "))
side3 = int(input("Enter the third side of the triangle: "))
perimeter = side1 + side2 + side3
print("Perimeter of the triangle is:",perimeter)

print("\nArea of square Calculation")
side = int(input("Enter the side of the square: "))
area = side * side
print("Area of the square is:",area)

print("\nArea of square Calculation")
side = int(input("Enter the side of the square: "))
perimeter = 4 * side
print("Perimeter of the square is:",perimeter)