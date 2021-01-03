from random import randrange
velikost = 10
jidlo = [(2, 3, True)]


def mapa(vstup):
    jidlo_radek, jidlo_sloupec, je_extra = jidlo[0] 
    for cislo_radku in range(velikost):
        for cislo_sloupce in range(velikost):
            souradnice = (cislo_radku, cislo_sloupce)
            if souradnice in vstup:
                souradnice = "X"
            elif jidlo_radek == cislo_radku and jidlo_sloupec == cislo_sloupce:
                souradnice = "?"
            else:
                souradnice = "."
            print(souradnice, end=" ")
        print("\n")
    



def pohyb(vstup, strana):
    jidlo_radek, jidlo_sloupec, je_extra = jidlo[0]
    cislo_radku, cislo_sloupce = vstup[-1]


    if strana == "s":
        novy_bod = (cislo_radku - 1, cislo_sloupce)
        if (cislo_radku - 1) < 0 or cislo_sloupce < 0 or (cislo_radku - 1) > (velikost - 1) or (cislo_sloupce) > (velikost - 1):
            raise ValueError("Game over")
        elif novy_bod in vstup:
            raise ValueError("Game over")
        else:
            if (cislo_radku - 1) == jidlo_radek and cislo_sloupce == jidlo_sloupec:
                vstup.append(novy_bod)
                jidlo_radek = randrange(0, velikost)
                jidlo_sloupec = randrange(0, velikost)
                if (jidlo_radek, jidlo_sloupec) in vstup:
                    jidlo_radek = randrange(0, velikost)
                    jidlo_sloupec = randrange(0, velikost)
                else:
                    if je_extra == True:
                        jidlo.append((jidlo_radek, jidlo_sloupec, True))
                        pozice = jidlo.index(((cislo_radku - 1), cislo_sloupce, je_extra))
                        del jidlo[pozice]
                    else:
                        pozice = jidlo.index(((cislo_radku - 1), cislo_sloupce, je_extra))
                        del jidlo[pozice]
                
                
            else:
                vstup.append(novy_bod)
                del vstup[0]
        
   
    elif strana == "j":
        novy_bod = (cislo_radku + 1, cislo_sloupce)
        if (cislo_radku + 1) < 0 or cislo_sloupce < 0 or (cislo_radku + 1) > (velikost - 1) or (cislo_sloupce) > (velikost - 1):
            raise ValueError("Game over")
        elif novy_bod in vstup:
            raise ValueError("Game over")
        else:
            if (cislo_radku + 1) == jidlo_radek and cislo_sloupce == jidlo_sloupec:
                vstup.append(novy_bod)
                jidlo_radek, jidlo_sloupec, je_extra = jidlo[0]
                jidlo_radek = randrange(0, velikost)
                jidlo_sloupec = randrange(0, velikost)
                if (jidlo_radek, jidlo_sloupec) in vstup:
                    jidlo_radek = randrange(0, velikost)
                    jidlo_sloupec = randrange(0, velikost)
                else:
                    if je_extra == True:
                        jidlo.append((jidlo_radek, jidlo_sloupec, True))
                        pozice = jidlo.index(((cislo_radku + 1), cislo_sloupce, je_extra))
                        del jidlo[pozice]
                    else:
                        pozice = jidlo.index(((cislo_radku + 1), cislo_sloupce, je_extra))
                        del jidlo[pozice]
                    
                
            else:
                vstup.append(novy_bod)
                del vstup[0]
        
   
    elif strana == "v":
        novy_bod = (cislo_radku, cislo_sloupce + 1)
        if cislo_radku < 0 or (cislo_sloupce + 1) < 0 or cislo_radku > (velikost - 1) or (cislo_sloupce + 1) > (velikost - 1):
            raise ValueError("Game over")
        elif novy_bod in vstup:
            raise ValueError("Game over")
        else:
            if cislo_radku == jidlo_radek and (cislo_sloupce + 1) == jidlo_sloupec:
                vstup.append(novy_bod)
                jidlo_radek, jidlo_sloupec, je_extra = jidlo[0]
                jidlo_radek = randrange(0, velikost)
                jidlo_sloupec = randrange(0, velikost)
                if (jidlo_radek, jidlo_sloupec) in vstup:
                    jidlo_radek = randrange(0, velikost)
                    jidlo_sloupec = randrange(0, velikost)
                else:
                    if je_extra == True:
                        jidlo.append((jidlo_radek, jidlo_sloupec, True))
                        pozice = jidlo.index((cislo_radku, (cislo_sloupce + 1), je_extra))
                        del jidlo[pozice]
                    else:
                        pozice = jidlo.index((cislo_radku, (cislo_sloupce + 1), je_extra))
                        del jidlo[pozice]
                
            else:
                vstup.append(novy_bod)
                del vstup[0]
        
   
    elif strana == "z":
        novy_bod = (cislo_radku, cislo_sloupce - 1)
        if cislo_radku < 0 or (cislo_sloupce - 1) < 0 or cislo_radku > (velikost - 1) or (cislo_sloupce - 1) > (velikost - 1):
            raise ValueError("Game over")
        elif novy_bod in vstup:
            raise ValueError("Game over")
        else:
            if cislo_radku == jidlo_radek and (cislo_sloupce - 1) == jidlo_sloupec:
                vstup.append(novy_bod)
                jidlo_radek, jidlo_sloupec, je_extra = jidlo[0]
                jidlo_radek = randrange(0, velikost)
                jidlo_sloupec = randrange(0, velikost)
                if (jidlo_radek, jidlo_sloupec) in vstup:
                    jidlo_radek = randrange(0, velikost)
                    jidlo_sloupec = randrange(0, velikost)
                else:
                    if je_extra == True:
                        jidlo.append((jidlo_radek, jidlo_sloupec, True))
                        pozice = jidlo.index((cislo_radku, (cislo_sloupce - 1), je_extra))
                        del jidlo[pozice]
                    else:
                        pozice = jidlo.index((cislo_radku, (cislo_sloupce - 1), je_extra))
                        del jidlo[pozice]
                
                
            else:
                vstup.append(novy_bod)
                del vstup[0]
        
    else:
        print("Zadej světovou stranu!")

vstup = [(0, 0), (0, 1), (0, 2)]
jidlo_radek, jidlo_sloupec, je_extra = jidlo[0]
jidlo_radek = randrange(0, velikost)
jidlo_sloupec = randrange(0, velikost)

while True:
    for i in range(30):
        strana = input("Na jakou světovou stranu chceš jet? ")
        pohyb(vstup, strana)
        mapa(vstup)
    jidlo.append((jidlo_radek, jidlo_sloupec, False))
