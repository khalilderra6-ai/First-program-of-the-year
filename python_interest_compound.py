principle = 0
time = 0
rate = 0

while True :
    principle = float(input("Enter the principle amount : "))
    if principle < 0 :
        print ("principle can't be negative pr equal to zero")
    else :
        break

while True :
    rate = float(input("Enter the interest rate : "))
    if rate < 0 :
        print ("Interest can't be negative pr equal to zero")
    else : 
        break

while True :
    time = int(input("Enter the time in years : "))
    if time < 0 :
        print ("time can't be negative pr equal to zero")
    else : 
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years : ${total:.2f}")