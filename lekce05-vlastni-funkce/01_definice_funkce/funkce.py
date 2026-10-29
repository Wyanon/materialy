def vypiš_čísla_do_max_hodnoty(jméno_volání, max_hodnota, ukaž_čáru=True):
    for aktualní_číslo in range(1, max_hodnota):
        print(jméno_volání, "," ,aktualní_číslo)
    if ukaž_čáru:
        print("-"*30)

vypiš_čísla_do_max_hodnoty("Volání A", 10)
vypiš_čísla_do_max_hodnoty("Volání B", 100)
vypiš_čísla_do_max_hodnoty("Volání C", 1000)


