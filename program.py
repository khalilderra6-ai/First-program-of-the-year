print("Hello world")
name = "Bro"
age = 21
GPA = 3.5
student = True

print(type(name))
print(type(age))
print(type(GPA))
print(type(student))
age = bool(age)
print(age)
name = input("Enter your name: ")
print(f"Hello {name}, you are {age} years old and your GPA is {GPA}.")

item = input("What item would like to buy: ")
price = float(input("What is the price of the item: "))
quantity = int(input("How many would you like to buy?: "))
total = price * quantity
print(f"You have bought {quantity} × {item}(s)\s")
print(f"Your total is : ${round(total, 2)}")
# Differents augmented assignment operators
# +=, -=, *=, /=, //=, **=, %=
# round() function is used to round a number to a specified number of decimal places
# if you want to round to the nearest whole number, you can use round(number) without specifying the number of decimal places.
# abs() function is used to return the absolute value of a number. It removes the negative sign from a number and returns its positive equivalent.
# pow function is used to raise a number to a specified power. It takes two arguments: the base and the exponent, and returns the result of raising the base to the power of the exponent.
# min and max functions are used to find the minimum and maximum values from a set of numbers. They can take multiple arguments or an iterable (like a list) and return the smallest or largest value, respectively.
