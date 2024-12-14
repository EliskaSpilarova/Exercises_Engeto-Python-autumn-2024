# Práce s listem
zamestnanci = [
    'František', 'Bruno',
    'Anna', 'Jakub',
    'Klára', 'Anežka',
    'Anežka', 'Anežka'
]
posledni_index = zamestnanci[-1]
print("Na indexu 2 je ", zamestnanci[2])
print("Na posledním indexu je ", posledni_index)
print("V intervalu od 2 do 5 je", zamestnanci[2:6])
print("Každý třetí člen je ", zamestnanci[::3])

# BMI index
jmeno = "Martin"
vaha = 80
vyska = 2
bmi = vaha/vyska ** 2

if bmi > 40:
    kategorie = "těžká obezita"
elif bmi > 30 and bmi < 40:
    kategorie = "obezita"
elif bmi > 25 and bmi > 30:
    kategorie = "mírná nadváha"
elif bmi < 25 and bmi > 18.5:
    kategorie = "normální váha"
elif bmi < 18.5:
    kategorie = "podvýživa"

print("Martine, tvoje bmi je", bmi, "což je", kategorie)

# List
zamestnanci_2 = ["František", "Anna", "Jakub", "Klára"]
print("Zaměstnanci na začátku:", zamestnanci_2)
zamestnanci_a = zamestnanci_2.copy()
zamestnanci_a.append("Bruno")
zamestnanci_a.append("Anežka")
print("Nová jména přidána:", zamestnanci_a)
zamestnanci_b = zamestnanci_2.copy()
zamestnanci_b.insert(1, "Bruno")
print("Nová jména vložena:", zamestnanci_b)

# Porovnání čísel
cislo_1 = float(input("Zadej první číslo"))
cislo_2 = float(input("Zadej druhé číslo"))
if cislo_1 > cislo_2:
    print("První číslo je větší než druhé")
elif cislo_1 < cislo_2:
    print("První číslo je menší než druhé číslo")
elif cislo_1 == cislo_2:
    print("Obě čísla jsou stejná")

