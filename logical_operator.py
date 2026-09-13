#or and nor
# or at least one condition must be true, and both conditions need to be true, not invert the condition

print("=== Convertisseur Poids & Température ===\n")

# ---------- Poids ----------
weight = float(input("Entrez votre poids : "))
unit = input("Unité (K pour kilogrammes / L pour pounds) : ").strip().upper()

# Utilisation de 'or' et 'not'
if unit == "K" or unit == "KG":
    converted = weight * 2.205
    print(f"Votre poids est {round(converted, 1)} lbs")
elif unit == "L" or unit == "LB" or unit == "LBS":
    converted = weight / 2.205
    print(f"Votre poids est {round(converted, 1)} kgs")
elif not unit:                          # si l'utilisateur n'a rien écrit
    print("Vous n'avez rien saisi !")
else:
    print(f"'{unit}' n'est pas une unité valide.")


print("\n" + "-" * 40 + "\n")


# ---------- Température ----------
measurement = input("Température en Celsius ou Fahrenheit (C/F) : ")
temp = float(input("Entrez la température : "))

# Utilisation de 'and', 'or' et 'not'
if measurement == "c" or measurement == "celsius":
    if temp >= -273.15 and temp <= 1000:          # plage raisonnable
        fahrenheit = (9 * temp) / 5 + 32
        print(f"{temp}°C = {round(fahrenheit, 1)}°F")
    else:
        print("Température hors de la plage acceptable.")
elif measurement == "f" or measurement == "fahrenheit":
    if not (temp < -459.67 or temp > 1800):       # même chose avec 'not' + 'or'
        celsius = (temp - 32) * 5 / 9
        print(f"{temp}°F = {round(celsius, 1)}°C")
    else:
        print("Température hors de la plage acceptable.")
else:
    print(f"'{measurement}' n'est pas valide. Utilisez C ou F.")