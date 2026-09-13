# General form = X if condition else Y
num = 678
result = "Even" if num % 2 == 0 else "ODD"
print(result)
a = 7
b = 6
age = 25
temperature = 20 



max_num = a if a > b else "b"
print(max_num)

status = "adult" if age >= 18 else "Teenager"
print(status)

weather = "HOT" if temperature >= 25 else "cold"
print(weather)

user_role = "admin"

acsess_role = "Full access" if user_role == "admin" else "No access"
print(acsess_role)



# ========== Useful string methods in Python ==========

name = "John Doe"

# 1. len() → counts the number of characters (including spaces)
print(len(name))                # 8

# 2. find() → searches for the FIRST position of a character/substring
#    Counting starts from 0
#    Returns -1 if the character is not found
print(name.find(" "))           # 4  (position of the space)
print(name.find("o"))           # 1  (first "o")
print(name.find("z"))           # -1 (not found)

# 3. rfind() → searches for the LAST occurrence of a character/substring
#    Also returns -1 if the character is not found
print(name.rfind("o"))          # 6  (last "o")
print(name.rfind(" "))          # 4
print(name.rfind("z"))          # -1

text = "hello world 123"

# ========== Case methods ==========

# 1. capitalize() → First letter uppercase, the rest lowercase
print(text.capitalize())        # "Hello world 123"

# 2. upper() → All letters to UPPERCASE
print(text.upper())             # "HELLO WORLD 123"

# 3. lower() → All letters to lowercase
print(text.lower())             # "hello world 123"


# ========== Checking methods (return True or False) ==========

# 4. isalpha() → True only if ALL characters are letters (no spaces, no numbers)
print("Hello".isalpha())        # True
print("Hello123".isalpha())     # False
print("Hello World".isalpha())  # False (because of the space)

# 5. isdigit() → True only if ALL characters are digits (0-9)
print("12345".isdigit())        # True
print("123abc".isdigit())       # False
print("12 34".isdigit())        # False (space)


# ========== Counting & Replacing ==========

# 6. count() → Counts how many times a character/substring appears
print(text.count("l"))          # 3
print(text.count("o"))          # 2
print(text.count("world"))      # 1
print(text.count("z"))          # 0

# 7. replace() → Replaces a character/substring with something else
print(text.replace("world", "Python"))   # "hello Python 123"
print(text.replace("l", "L"))            # "heLLo worLd 123"
print(text.replace(" ", "-"))            # "hello-world-123"

# print(help(str)) to see many other useful string methods


user_name = input("Enter your user_name")
user_name.find(" ")
user_name.isdigit()
if len(user_name) > 12 :
    print("Your user_name can't be more than 12 characters")
elif not user_name.find(" ") == -1 :
    print("Your user_name can't contain spaces")
elif  not user_name.isdigit() == False :
    print("Your user_name must not contain digits")
else :
    print(f"Welcome {user_name}")