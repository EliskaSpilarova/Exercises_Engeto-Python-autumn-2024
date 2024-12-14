# Počet souhlásek a samohlásek
veta = "Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu"
samohlasky = "aeiouáéíóú"
souhlasky = "bcčdďfghjklmnňprřsštťvzžcdž"
vysledek = {"souhlasky":0, "samohlasky":0} #klíče souhlásky a samohlásky

for znak in veta.lower():  
    if znak in samohlasky:
        vysledek["samohlasky"] += 1
    elif znak in souhlasky:
        vysledek["souhlasky"] += 1

print("Pocet samohlasek:", vysledek["samohlasky"])
print("Pocet souhlasek:", vysledek["souhlasky"])

# Počet sudých a lichých čísel
cisla = [1, 2, 3, 4, 5, 6, 7, 8]
suda = 0
licha = 0

for cislo in cisla:
    if cislo % 2 == 0:
        suda = suda + cislo
    else:
        licha = licha + cislo

vysledek = abs(suda - licha)
print("Rozdíl je", vysledek)

# Slovníková komprehence
seznam_slov = ["jablko", "pomeranč", "banán", "kiwi", "hruška"]
delky_slov = {slovo: len(slovo) for slovo in seznam_slov}
print("Délky slov:", delky_slov)