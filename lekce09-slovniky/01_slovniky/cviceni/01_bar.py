# Cvičení 1 – Slovníky
# Doplň kód pod zadání a soubor spusť (Run).

# Na večírku je bar a tohle je jeho ceník. Postupně:
#    - vypiš, kolik stojí voda,
#    - přidej colu za 40 Kč,
#    - zdraž pivo o 5 Kč,
#    - vodu odeber, došla,
#    - vypiš celý ceník a kolik položek v něm je.
#
#      Voda stojí 20 Kč.
#      {'pivo': 50, 'víno': 60, 'džus': 35, 'cola': 40}
#      Položek: 4

cenik = {"pivo": 45, "víno": 60, "džus": 35, "voda": 20}
print(f"Voda stojí {cenik['voda']} Kč.")
cenik.update({"cola": 40})
cenik["pivo"] += 5
del cenik["voda"]
print(cenik)
print(f"Položek: {len(cenik)}")