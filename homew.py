
# Exo 1 : Convertir un texte en minuscules

texte = input("Entrez un texte : ")
print(texte.lower())
 
# Exo 2 : Remplacer les espaces par des underscores

texte = input("Entrez un texte : ")
resultat = texte.replace(" ", "_")
print(resultat)
 
# Exo 3 : Calcul de l'énergie selon la formule E = mc^2

m = int(input("Entrez la masse en kg : "))
c = 300_000_000
E = m * c ** 2

print(f"The energy corresponding to a mass of {m} kg is {E} Joules")
 
# Exo 4 : Conversion Celsius vers Fahrenheit

def celsius_to_float(c):
    return float(c)

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def main():
    celsius = celsius_to_float(input("Temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")

main()
 
# Exo 6 : Calculatrice

expression = input("Entrez une expression (ex: 5 + 3) : ")

x, op, y = expression.split()
x = float(x)
y = float(y)

if op == "+":
    result = x + y
elif op == "-":
    result = x - y
elif op == "*":
    result = x * y
elif op == "/":
    result = x / y
else:
    result = "Opérateur invalide"

print(f"{result:.1f}")
 
# Exo 7 : Study Schedule

def convert(time):
    h, m = time.split(":")
    return int(h) + int(m) / 60

def main():
    time = input("Enter time (HH:MM): ")
    t = convert(time)

    if 7 <= t <= 9:
        print("Focus session")
    elif 14 <= t <= 16:
        print("Review session")
    elif 22 <= t <= 24:
        print("Coding session")
    else:
        print("Break time")

main()
 
# Exo 8 : Détecteur de type de fichier

filename = input("Nom du fichier : ").lower()

if filename.endswith(".py"):
    print("Python script")
elif filename.endswith(".java"):
    print("Java program")
else:
    print("Type de fichier inconnu")
 
# Exo 9 : Conversion camelCase vers snake_case

camel = input("Entrez un nom en camelCase : ")
snake = ""

for char in camel:
    if char.isupper():
        snake += "_" + char.lower()
    else:
        snake += char

print(snake)
 
# Exo 10 : Suppression des voyelles

texte = input("Entrez un texte : ")
voyelles = "aeiouAEIOU"

resultat = ""
for c in texte:
    if c not in voyelles:
        resultat += c

print(resultat)
 
# Bonus 1 : Validation d'email avec regex

import re

def is_valid_email(email):
    pattern = r'^[A-Za-z0-9._]+@[A-Za-z0-9]+\.(com|dz|edu)$'
    return re.match(pattern, email) is not None

def main():
    email = input("Email: ")
    if is_valid_email(email):
        print("Valid")
    else:
        print("Invalid")

main()
 
# Bonus 3 : Gestion des notes avec fichiers

def main():
    with open("grades.txt", "r") as f:
        lines = f.readlines()

    with open("results.txt", "w") as out:
        for line in lines:
            parts = line.split()
            name = parts[0]
            grades = list(map(int, parts[1:]))

            average = sum(grades) / len(grades)
            out.write(f"{name}: {average:.1f}\n")

main()
 
  #exo5:
answer = input().strip().lower()

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")