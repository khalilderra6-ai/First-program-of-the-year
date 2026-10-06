name = int(input("Enter a number : "))

try:
    result = 10 / name
except ZeroDivisionError:
    print("error : Division by zero")
finally :
    print("This will always print")