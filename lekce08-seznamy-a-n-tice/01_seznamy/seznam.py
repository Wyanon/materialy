hoste = ["Marta", "Shrek", "Petr Pavel"]
print(hoste)            # ['Marta', 'Shrek', 'Petr Pavel']

organizator = "Karel"
organizator = organizator.upper() + " Gott"     # KAREL GOTT
print(organizator, "zve", hoste, "na vanocni vecirek.")
print("Na večírek je pozváno", len(hoste), "hostů.")
pozvanka = "Zvu Vás na svůj vanoční večírek." + organizator[0] + organizator[6]
print(pozvanka)

for i in range(len(hoste)):
    host = hoste[i]
    print("Zveme Vás na vánoční večírek" , hoste[i])


print("První byl/a pozvan/a", hoste[0])       
blacklist = ["Hegerová" , "Vlk"]
prichozi = input("Jak se jmenuješ?") 
for host in hoste:
    prichozi == hoste
    print("Pojd dál!" , prichozi) 
     # Marta

def kontrola(prichozi):
    if prichozi in hoste:
        print("Pojď dál!", prichozi)
    elif prichozi in blacklist:
        print("Nejsi zván/a!", prichozi)
    else:
        print("Neznám tě.", prichozi)

kontrola(prichozi, hoste, blacklist)

def pozvi(jmeno, hoste):
    if jmeno not in hoste:
        hoste.append(jmeno)
        print("Pozván/a", jmeno)
    else:
        print(jmeno, "už je pozván/a.")

print(organizator.split())
rozdelene_jmeno = organizator.split()[0][0] + organizator.split()[1][0]
print(inicialy)