
from random import randrange

slovo = "trávník", "stromek", "stavení"
cislo = randrange(0, 3)
neuspesne_pokusy = 0

if cislo == 0:
    slovo = "trávník"
elif cislo == 1:
    slovo = "stromek"
else:
    slovo = "stavení"
    
skryte_slovo = str("_" * len(slovo))
print(skryte_slovo)

while neuspesne_pokusy < 9:
    pismeno = input("Jaké sis zvolil písmeno? ")
    if pismeno in slovo:
        pozice = slovo.index(pismeno)
        zacatek = skryte_slovo[:pozice]
        konec = skryte_slovo[pozice + 1:]
        skryte_slovo = zacatek + pismeno + konec
        print(skryte_slovo)
    else:
        neuspesne_pokusy = neuspesne_pokusy + 1
    print("Neúspěšné pokusy: ", neuspesne_pokusy)
    if "_" not in skryte_slovo:
        print("Gratuluji, vyhrál jsi!")
        break
if neuspesne_pokusy >= 9:
    print("Prohrál jsi, konec hry!")

