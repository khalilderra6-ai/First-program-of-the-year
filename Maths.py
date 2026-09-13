import math
print("The value of pi is:", math.pi)
print("The value of e is:", math.e)
x = 64
result = math.sqrt(x)
print(f"The square root of {x} is: {result}")
# ceil() function is used to round a number up to the nearest integer. It takes a single argument, which is the number you want to round up, and returns the smallest integer greater than or equal to that number.
#floor() function is used to round a number down to the nearest integer. It takes a single argument, which is the number you want to round down, and returns the largest integer less than or equal to that number.
y = 3.7
print(f"The ceiling of {y} is : {math.ceil(y)}")
print(f"The floor of {y} is : {math.floor(y)}")

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is : {round(circumference, 2)} cm")
area = math.pi * radius ** 2
print(f"The area of the circle is : {round(area, 2)} cm²")

a = float(input("Enter the side a of the triangle: "))
b = float(input("Enter the side b of the triangle: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print (f"The length of the hypotenuse c is : {round(c,2)}cm" )

                                               

                                                