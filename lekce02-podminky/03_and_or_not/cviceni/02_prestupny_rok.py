# Cvičení 2 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Přestupný rok. Rok je přestupný, když je dělitelný čtyřmi,
#    ale ne stovkou – NEBO když je dělitelný čtyřmi sty.
#    Zeptej se na rok a vypiš "Přestupný." / "Nepřestupný.".
#    (Vyzkoušej 2024, 1900, 2000.)
if int(input("Zadej rok: ")) % 4 == 0 and int(input("Zadej rok: ")) % 100 != 0 or int(input("Zadej rok: ")) % 400 == 0:
    print("Přestupný.")
else:
    print("Nepřestupný.")

