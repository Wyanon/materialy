def cena_mhd(věk):
    print("Pocitam cenu listku pro vek", věk)
    if věk < 6:
       print("Cena listku je 0 Kc")
       return 0
    elif věk < 18: 
         print("Cena listku je 39 Kc")
         return 39
    elif věk < 65:
         print("Cena listku je 50 Kc")  
         return 50
    else:
         print("Cena listku je 0 Kc")
         return 0

zustatek_uctu = 100
cena_jizdenky =cena_mhd(7)
print("Vysledna_cena_je", cena_jizdenky)
cena_jizdenky = cena_jizdenky*1.5

zustatek_uctu = zustatek_uctu - cena_jizdenky
print("Zustatek uctu je", zustatek_uctu)