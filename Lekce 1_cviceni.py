# Slicing, striding
slovo = 'indexování'
print("Prvních pět písmen slova: ", slovo[:5])
print("Posledních pět písmen slova: ", slovo[-5:])
print("Každé třetí písmeno slova: ", slovo[::3])

# Převaděč jednotek
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

kg_pocet = 80
km_pocet = 54
l_pocet = 5

kg_vysledek = kg_lb * kg_pocet
km_vysledek = km_mile * km_pocet
l_vysledek = l_gal * l_pocet 

print(kg_pocet,  "kg", "je", kg_vysledek, "lb")
print(km_pocet, "km", "je", km_vysledek, "mil")
print(l_pocet, "l", "je", l_vysledek, "gal")

# Cena aut
mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000
sleva_merc = 5000
print("Sleva na Mercedes je", sleva_merc)
cena_2_merc = mercedes * 2
print("Cena za dva Mercedesy je", cena_2_merc)
cena_merc_a_rolls = mercedes + rolls_royce
print("Cena za Mercedes a Rolls-Royce je", cena_merc_a_rolls)
cena_2_rolls_s_vybavou = (rolls_royce * 2) + (vybava * 2)
print("Cena za dva Rolls-Royce s příplatkovou výbavou je", cena_2_rolls_s_vybavou)
cena_merc_s_vybavou = mercedes + vybava
print("Cena za Mercedes s příplatkovou výbavou je", cena_merc_s_vybavou)
merc_se_slevou = mercedes - sleva_merc
print("Cena za Mercedes po slevě je", merc_se_slevou)

# Výpis osoby
jmeno = "Lukáš"
prijmeni = "Dvořák"
cele_jmeno = jmeno+ " " + prijmeni
delka_jmena  = len(cele_jmeno)

print("Celé jméno: ", cele_jmeno)
print("Délka jména: ", delka_jmena)
print("=" * delka_jmena)
print(cele_jmeno)
print("=" * delka_jmena)


