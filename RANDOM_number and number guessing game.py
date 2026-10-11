import random

options = ("rock", "papers", "scissors")
cards = ["2", "3","4","5","6","7","8","9","10","j","k","q","A"]

#number = random.randint(1, 6)
#number = random.randint(low, high) can be used with variables
#number = random.random() a float number between 0 and 1
# option = random.choice(options)
#random.shuffle(cards)

low = 1
high = 100

number = random.randint(low, high)

guesses = 0
while True :
    guess = int(input(f"Enter a number between {low} - {high} : "))
    guesses += 1
    if guess < number :
        print(f"{guess} is too low")
    elif guesses > number :
        print(f"{guess} is too high")
    else :
        print(f"{guess} is correct !")
        break

print(f"This round took you {guesses} guesses ")



