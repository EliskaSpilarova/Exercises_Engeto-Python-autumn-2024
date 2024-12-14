# Slovníky
user_email = {"email":"marek.parek@gmail.com"}
user_1 = dict()
user_1 = {"name":"Marek", "surname":"Parek"}
user_1.update(user_email)
print("User01:", user_1)

# Heslo zadané uživatelem
jmeno = 'Marek'
heslo = '1234'
uzivatel = {'Marek': '1234'}

if uzivatel.get(jmeno) == heslo:
    print("Ahoj Marek vítej v aplikaci! Pokračuj...")
else:
    print("Uživatelské jméno nebo heslo nejsou v pořádku!")

# Sety
cisla_1 = (1, 1, 2, 3, 4)
cisla_2 = (5, 6, 7, 7, 8)  
cisla_3 = set(cisla_1)
cisla_4 = set(cisla_2)
print(("Sjednocené hodnoty ze zadání: ", cisla_3.union(cisla_4))) 

# Rozdíl proměnných
cisla_1 = {1, 2, 3, 4}
cisla_2 = {3, 4, 5, 6}
rozdil_cisel = cisla_1.difference(cisla_2)
print("Rozdílné hodnoty prvního setu oproti druhému", rozdil_cisel)

#Práce se slovníkem
slovnik = {
    "kočka": "cat",
    "pes": "dog",
    "strom": "tree",
    "auto": "car",
    "dům": "house"
}
pocet_slov = len(slovnik)
print("Počet slov ve slovníku je", pocet_slov)
ceska_slova = slovnik.keys()
print(ceska_slova)
anglicka_slova = slovnik.values()
print(anglicka_slova)
nove_ceske_slovo = input("Zadej české slovo")
nove_anglicke_slovo = input("Zadej anglický překlad")
slovnik.update({nove_ceske_slovo: nove_anglicke_slovo})
print(slovnik)
odstranene_slovo = input("Zadej slovo k odstranění")
slovnik.pop(odstranene_slovo)
print("Aktualizovaný slovník:", slovnik)

# Množiny
mnozina_1 = {"kočka", "pes", "králík", "had"}
mnozina_2 = {"pes", "papoušek", "had", "ryba"}
print(len(mnozina_1))
print(len(mnozina_2))
print(mnozina_1.difference(mnozina_2))
print(mnozina_2.difference(mnozina_1))
print(mnozina_1.intersection(mnozina_2))
print(mnozina_1.union(mnozina_2))
nove_zvire = (input("Vlož nové zvíře:"))
mnozina_1.add(nove_zvire)
print(mnozina_1)
dalsi_zvire = (input("Vlož další zvíře"))
mnozina_2.add(dalsi_zvire)
print(mnozina_1, mnozina_2)