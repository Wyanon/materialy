def je_heslo_dlouhe(heslo):


def zeptej_se_na_jmeno():
    jmeno = input("Zadej jméno: ")
    return jmeno

def zeptej_se_na_heslo():
    heslo = input("Zadej heslo: ")
    return heslo

def prihlaseni(jmeno, heslo):
    jmeno = input("Zadej jméno: ")
    heslo = input("Zadej heslo: ")
    if len(heslo) > 8:
        print("Vítej, " + jmeno + "!")
    else:
        print("Heslo je příliš krátké")


