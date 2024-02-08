#projekt_1.py: první projekt do Engeto Online Python Akademie

#author: Jiří Knotek
#email: jiriknotek42@gmail.com
#discord: jirka420666

import re


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

registrovani_uzivatele = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

def analyzovat_text(text):
    slova = re.findall(r'\b\w+\b', text)
    
    delky_slov = [len(slovo) for slovo in slova]
    vyskyty_delky_slov = {delka: delky_slov.count(delka) for delka in set(delky_slov)}

    slova_s_velkym_pismenem = [slovo for slovo in slova if slovo.istitle()]
    slova_velkymi_pismeny = [slovo for slovo in slova if slovo.isupper()]
    slova_malymi_pismeny = [slovo for slovo in slova if slovo.islower()]
    
    numericke_retezce = [slovo for slovo in slova if slovo.isnumeric()]
    soucet_cisel = sum(int(cislo) for cislo in numericke_retezce)

    return {
        'pocet_slov': len(slova),
        'pocet_slov_s_velkym_pismenem': len(slova_s_velkym_pismenem),
        'pocet_slov_velkymi_pismeny': len(slova_velkymi_pismeny),
        'pocet_slov_malymi_pismeny': len(slova_malymi_pismeny),
        'pocet_numericke_retezce': len(numericke_retezce),
        'soucet_cisel': soucet_cisel,
        'vyskyty_delky_slov': vyskyty_delky_slov
    }

def zobrazit_histogram(vyskyty_delky_slov):
    print("DELKA| VYSKYTY     |POCET")
    print("-" * 40)

    for delka, pocet in sorted(vyskyty_delky_slov.items()):
        print(f"{delka:5}| {'*' * pocet:13}| {pocet}")

def hlavni():
    uzivatelske_jmeno = input("Uzivatelske jmeno: ")
    heslo = input("Heslo: ")

    if uzivatelske_jmeno in registrovani_uzivatele and heslo == registrovani_uzivatele[uzivatelske_jmeno]:
        print("-" * 40)

        print(f"Vitejte v aplikaci, {uzivatelske_jmeno}")
        print(f"Mame {len(TEXTS)} textu k analyze.")
        print("-" * 40)


        cislo_textu = input("Zadejte cislo od 1 do 4 pro vyber: ")

        if cislo_textu.isdigit() and 1 <= int(cislo_textu) <= 4:
            vybrany_text = TEXTS[int(cislo_textu) - 1]
            vysledek_analyzy = analyzovat_text(vybrany_text)

            print("-" * 40)
            print(f"V textu je {vysledek_analyzy['pocet_slov']} slov.")
            print(f"Je zde {vysledek_analyzy['pocet_slov_s_velkym_pismenem']} slov začínajících velkým písmenem.")
            print(f"Je zde {vysledek_analyzy['pocet_slov_velkymi_pismeny']} slov psaných velkými písmeny.")
            print(f"Je zde {vysledek_analyzy['pocet_slov_malymi_pismeny']} slov psaných malými písmeny.")
            print(f"Je zde {vysledek_analyzy['pocet_numericke_retezce']} numerických řetězců.")
            print(f"Součet všech čísel: {vysledek_analyzy['soucet_cisel']}")
            print("-" * 40)
            zobrazit_histogram(vysledek_analyzy['vyskyty_delky_slov'])

        else:
            print("Neplatný vstup. Zadejte číslo od 1 do 4.")
    else:
        print("Neregistrovaný uživatel, ukončuji program.")

if __name__ == "__main__":
    hlavni()


