jmeno = input("Zadej jmeno")

rovna_se = "A" == "a"
print(rovna_se)


kniha = "Malý princ!" \
"stran_celkem = 320" \
"precteno = 183" \
"print(f"V {kniha} zbyva {stran_celkemprecteno} stran z celkem {stran_celkem} stran.")"

def procenta(cast, celek):
    return cast / celek * 100
print(f"Mas precteno {procenta(precteno, stran_celkem)} % knihy {kniha}.")