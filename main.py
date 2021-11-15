#!/usr/bin/env python3
############################################################################
# Soubor:  main.py
# Datum:
# Autor:
############################################################################
from random import randint, choice

############################################################################


def menu():
    try:
        prvni_soubor = input("Zadejte první soubor: ")
        druhy_soubor = input("Zadejte druhý soubor: ")
        f1 = open(prvni_soubor, "r")
        f2 = open(druhy_soubor, "w")
    except FileNotFoundError:
        print("Zadal jsi špatný soubor.")

    while True:
        print("""
        1 - Převede soubor na malá písmena.
        2 - Nahradí výskyt zadaného znaku v souboru 2 (musí v něm něco být !!) jiným zadaný znakem.
        3 - Statistika výskytu jednotlivých znaků v souboru 1.
        4 - Generování náhodného textu.
        """)
        volba = input("jakou akci chcete provést? ")
        if volba == "1":
            prevod_pismen(f1, f2)

        elif volba == "2":
            nahrazeni(f1, f2, input("Zadej znak1, kterej chceš aby se změnil "), input("Zadej znak2, kterým změníš znak 1 "))

        elif volba == "3":
            statistika(f1)

        elif volba == "4":
            maxwords = int(input("Zadej počet slov: "))
            while maxwords < 1:
                print("Zadal jsi neplatný číslo ty pimpulíne!")
                maxwords = int(input("Zadej počet slov: "))
            print(sentence_gen(maxwords))

def prevod_pismen(file1, file2):
    for line in file1:
        file2.write(line.lower())


def nahrazeni(file1, file2, znak1, znak2):
    while True:
        pismeno = file1.read(1)
        if pismeno == "":
            break
        else:
            if pismeno.upper() == znak1.upper():  #Ošetření malých/velkých písmen
                file2.write(znak2)
            else:
                file2.write(pismeno)


def statistika(file1):
    znaky = {}
    while True:
        pismeno = file1.read(1)
        if pismeno == "":
            file1.seek(0)
            break
        else:
            if pismeno not in znaky.keys():
                znaky[pismeno] = 1
            else:
                znaky[pismeno] += 1
    for key in sorted(znaky.keys()):
        if key == "\n":
            print(f"(\\n) --- {znaky[key]}")
        else:
            print(f"({key}) --- {znaky[key]}")


def word_gen(minchars=2, maxchars=10):
    vysledek = ""
    samohlasky = "aeiyou"
    souhlasky = "qwrtpsdfghjklzxcvbnm"
    pocet = randint(minchars, maxchars)
    zacatek = randint(0, 1)
    for i in range(pocet):
        if i % 2 == zacatek:
            vysledek = vysledek + choice(samohlasky)
        else:
            vysledek = vysledek + choice(souhlasky)
            if randint(1, 10) == 1:  # dvě souhlásky vedle sebe
                vysledek = vysledek + choice(souhlasky)
    return vysledek


def sentence_gen(maxwords):
    vysledek = ""
    for i in range(maxwords):
        vysledek = vysledek + word_gen() + " "
    return vysledek.capitalize()[0:-1] + "."


if __name__ == "__main__":
    menu()
