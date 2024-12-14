# Součin číselných hodnot
prvni_cislo = 5
druhe_cislo = 5

def vynasob (num1, num2):
    return num1 * num2

vysledek = vynasob(prvni_cislo, druhe_cislo)
print("Výsledek je", vysledek)

# Zdvojnásobení
vstup = "Ahoj všem"

def zdvojnasob_vsechny_znaky(vstup):
    vysledek = ""
    for znak in vstup:
        vysledek += znak * 2
    return vysledek


vysledek = zdvojnasob_vsechny_znaky(vstup)
print(vysledek)

# Ověření OS
import sys

def je_os_windows():
    return sys.platform == "win32"

vysledek = je_os_windows()
print(vysledek)