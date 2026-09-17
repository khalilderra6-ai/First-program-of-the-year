# indexing = accesing of some elements in sequence use in []

 #[start : end : step]

credit_number = "1234-5678-9087"

 #print(credit_number[0])
print(credit_number[0:4])
print(credit_number[0:]) #listing all the elements since the start
print(credit_number[0:4])
print(credit_number[-1])
print(credit_number[: : 2]) #counting the characthers 2 by 2

last_digits = credit_number[-4 :]
print(f"XXXX-XXXx-{last_digits}")

email = input("Enter your email : ")

username = email[ :email.index('@') ] 
domain = email[email.index('@')+ 1 :]

print(f"votre username est {username} et votre domain est {domain}")
