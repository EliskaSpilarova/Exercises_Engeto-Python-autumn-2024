# Délka slov
slova = []

while len(slova) < 3:
    slovo = input("Zadej slovo: ")

    if len(slovo) != 4:
        print("Slovo není dlouhé čtyři znaky")
        continue

    if slovo in slova:
        print("Slovo už je uložené")
    else:
        slova.append(slovo)

print("Už mám uložené tři slova.")

# Výběr z hodnot
ovoce = ["jablko", "banan", "citron", "pomeranc"]

print("Dostupné ovoce: ", ", ".join(ovoce))

while True:
    vyber = input("VYBER Z DOSTUPNÉHO OVOCE: ")
    if vyber in ovoce:
        print("Bezva, toto ovoce je v nabídce.")
        break
    else:
        print("Ovoce není v nabídce.")

# Aritmetické operátory
while True:
    operation = input("Zadejte operátor (+ nebo -): ")
    if operation not in ["+", "-"]:
        print("Nezadali jste platný operátor, zkuste to znovu.")
        continue

    number_1 = float(input("Zadejte první číslo: "))
    number_2 = float(input("Zadejte druhé číslo: "))

    if operation == "+":
        result = number_1 + number_2
    elif operation == "-":
        result = number_1 - number_2

    print(f"{number_1} {operation} {number_2} = {result}")

    dalsi = input("Chcete provést další operaci? (ano/ne): ").strip().lower()
    if dalsi != "ano":
        print("Děkujeme za použití kalkulačky.")
        break
