age = int(input("Enter your age: "))

if age > 100 :
    print("You are too old to sign up")

elif age >= 18  :
    print("You signed up successfully")
elif age <0:
    print("You are not born yet")
else:
    print("You must be at least 18 years old to sign up")

name = input("Enter your name: ")
if name == "":
    print("You must enter your name")
else :
    print(f"hello {name},Welcome here and have a great time learning python programming")


for_sale = True 
if for_sale:
    print ("This item is for sale")
else:
    print("This item is not for sale")
    

