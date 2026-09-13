# Weight converter
weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds (K or L): ").strip().upper()

if unit == "K":
    converted = weight * 2.205
    print(f"Your weight is {round(converted, 1)} lbs")
elif unit == "L":
    converted = weight / 2.205
    print(f"Your weight is {round(converted, 1)} kgs")
else:
    print(f"'{unit}' is not a valid unit. Please enter K or L.")


# Temperature converter
measurement = input("Is the temperature in Celsius or Fahrenheit (C/F): ").strip().lower()
temp = float(input("Enter the temperature: "))

if measurement == "c":
    converted = (9 * temp) / 5 + 32
    print(f"The temperature in Fahrenheit is {round(converted, 1)}°F")
elif measurement == "f":
    converted = (temp - 32) * 5 / 9
    print(f"The temperature in Celsius is {round(converted, 1)}°C")
else:
    print(f"'{measurement}' is not valid. Please enter C or F.")