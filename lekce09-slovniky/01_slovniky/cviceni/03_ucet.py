# Cvičení 3 – Slovníky
# Doplň kód pod zadání a soubor spusť (Run).

# Petra si u baru objednala několik nápojů. Spočítej, kolik zaplatí.
#    Nápoj, který v ceníku není, nepočítej a vypiš "Tohle nemáme: ...".
#
#      Tohle nemáme: šampaňské
#      Celkem: 185 Kč

cenik = {"pivo": 45, "víno": 60, "džus": 35, "voda": 20}
objednavka = ["pivo", "víno", "šampaňské", "pivo", "džus"]
celkem = 0
for napoj in objednavka:
    if napoj in cenik:
        celkem = celkem + cenik[napoj]
    else:
        print(f"Tohle nemáme: {napoj}")
        
print(f"Celkem: {celkem} Kč")