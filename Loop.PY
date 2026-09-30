name = input ("Enter your name :")

while name == "" :
    print("You did not enter your name")
    name = input ("Enter your name :")


print(f"Hello {name}") 

age = int(input("Enter your age : "))

while age < 0 :
    print(f"age can't be negative")
    age = int(input("Enter your age : "))

print(f"You are {age} years old ")    

food = input("Enter a food you like (q to quit)")

while not food == 'q' :
    print(f"You like {food}")
    food = input("Enter another food you like")

print("Bye")    


num = int(input("Enter a number (between 1 and 10 : )"))

while num < 0 or num > 13 :
    print(f"{num} is mot valid")
    num = int(input("Enter a number (between 1 and 10 : )"))

print(f"Your num is {num}")
