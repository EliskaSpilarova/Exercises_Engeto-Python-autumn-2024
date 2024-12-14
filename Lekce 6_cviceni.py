# Kámen, nůžky, papír
import random

moznosti = ['kamen', 'nuzky', 'papir']

hrac = "kamen"
pocitac = random.choice(moznosti)

print(f"Hráč: {hrac}")
print(f"Počítač: {pocitac}")

if hrac == pocitac:
    print("Nerozhodně.")
elif (hrac == 'kamen' and pocitac == 'nuzky') or \
     (hrac == 'nuzky' and pocitac == 'papir') or \
     (hrac == 'papir' and pocitac == 'kamen'):
    print("Vyhrál jsi!")
else:
    print("Prohrál jsi:(")

# Tři prázdné adresáře
import os

jmena_slozek = ["obrazky", "texty", "gify"]

for slozka in jmena_slozek:
    if os.path.exists(slozka) and os.path.isdir(slozka):
        print("Složka již existuje!")
    else:
        os.mkdir(slozka)
        print(f"Tvořím novou složku: {slozka}")

print("Všechny složky existují.")

# Házení kostkou
import random

min_hodnota = 1
max_hodnota = 6

while True:
    print("Házím kostkou...")
    kostka_hodnota = random.randint(min_hodnota, max_hodnota)
    print(f"Na kostce je: {kostka_hodnota}")
    
    if kostka_hodnota == 6:
        continue
    else:
        break
