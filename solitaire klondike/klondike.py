import random

def vytvor_balicek():
    """Vrátí balíček 52 karet – od esa (1) po krále (13) ve čtyřech barvách

    Všechny karty jsou otočené rubem nahoru.
    """
    balicek = []
    for hodnota in range(1, 14):
        for barva in "Sr", "Ka", "Pi", "Kr":
            balicek.append((hodnota, barva, False))
    random.shuffle(balicek)
    return balicek

from karty import popis_kartu

def popis_balicek(karty):
    """Vrátí popis všech karet v balíčku. Jednotlivé karty odděluje mezerami.
    """
    popsany_balicek = []
    
    for karta in karty:
        popsana_karta = popis_kartu(karta)
        popsany_balicek.append(popsana_karta)

    vysledny_balicek = ' '.join(popsany_balicek)
    return vysledny_balicek

def popis_vrchni_kartu(balicek):
    """Vrátí popis daného balíčku karet -- tedy vrchní karty, která je vidět."""
    if balicek == []:
        popsana_karta = "[   ]"
    else:
        karta = balicek[-1]
        popsana_karta = popis_kartu(karta)
    return popsana_karta

from karty import otoc_kartu

def rozdej_sloupecky(balicek):
    """Rozdá z daného balíčku 7 "sloupečků" -- seznamů karet

    Karty ve sloupečcích jsou odstraněny z balíčku.
    Vrátí všechny sloupečky -- tedy seznam (nebo n-tici) sedmi seznamů.
    """
    seznam_vsech_sloupcu = []
    for N in range(0, 7):
        sloupec = []
        for i in range(N):
            vybrana_karta = balicek.pop()
            sloupec.append(vybrana_karta)
        posledni_karta = balicek.pop()
        posledni_karta = otoc_kartu(posledni_karta, True)
        sloupec.append(posledni_karta)
        seznam_vsech_sloupcu.append(sloupec)
    return seznam_vsech_sloupcu

balicek = vytvor_balicek()
sloupecky = rozdej_sloupecky(balicek)

from itertools import zip_longest

def vypis_sloupecky(sloupecky):
    """Vypíše sloupečky textově.

    Tato funkce je jen pro zobrazení, používá proto přímo funkci print()
    a nic nevrací.
    """
 
    S0, S1, S2, S3, S4, S5, S6 = sloupecky
    if S0 == [] and S1 == [] and S2 == [] and S3 == [] and S4 == [] and S5 == [] and S6 == []:
        print("")
        return
    else:
        S0p = []
        for karta in S0:
            popsana_karta = popis_kartu(karta)
            S0p.append(popsana_karta)
        
        S1p = []
        for karta in S1:
            popsana_karta = popis_kartu(karta)
            S1p.append(popsana_karta)
        
        S2p = []
        for karta in S2:
            popsana_karta = popis_kartu(karta)
            S2p.append(popsana_karta)
        
        S3p = []
        for karta in S3:
            popsana_karta = popis_kartu(karta)
            S3p.append(popsana_karta)

        S4p = []
        for karta in S4:
            popsana_karta = popis_kartu(karta)
            S4p.append(popsana_karta)

        S5p = []
        for karta in S5:
            popsana_karta = popis_kartu(karta)
            S5p.append(popsana_karta)

        S6p = []
        for karta in S6:
            popsana_karta = popis_kartu(karta)
            S6p.append(popsana_karta)



    sloucene_sloupce = list(zip_longest(S0p, S1p, S2p, S3p, S4p, S5p, S6p, fillvalue='     '))

    for i in sloucene_sloupce:
        print(*i)


def presun_kartu(sloupec_odkud, sloupec_kam, pozadovane_otoceni):
    """Přesune vrchní kartu ze sloupce "odkud" do sloupce "kam".
    Karta bude otocena lícem nebo rubem nahoru podle "pozadovane_otoceni".
    """
    presunovana_karta = sloupec_odkud.pop()
    presunovana_karta = otoc_kartu(presunovana_karta, pozadovane_otoceni)
    sloupec_kam.append(presunovana_karta)
    return sloupec_odkud, sloupec_kam

def presun_nekolik_karet(sloupec_odkud, sloupec_kam, pocet):
    """Přesune "pocet" vrchních karet ze sloupce "odkud" do sloupce "kam".
    Karty se přitom neotáčí.
    """
    n = int(pocet)
    if n == 1:
        presunovane_karty = sloupec_odkud.pop()
        sloupec_kam.append(presunovane_karty)
        
    else:    
        presunovane_karty = []
        for i in range(n):
            odebrana_karta = sloupec_odkud.pop()
            presunovane_karty.append(odebrana_karta)
        presunovane_karty.reverse()
        sloupec_kam.extend(presunovane_karty)
 
    return sloupec_odkud

def udelej_hru():
    """Vrátí slovník reprezentující novou hru.
    """
    balicek = vytvor_balicek()

    hra = {
        'U': balicek,
    }

    # V-Z začínají jako prázdné seznamy
    for pismenko in 'VWXYZ':
        hra[pismenko] = []

    # A-G jsou sloupečky
    for pismenko, sloupec in zip('ABCDEFG', rozdej_sloupecky(balicek)):
        hra[pismenko] = sloupec

    return hra

def vypis_hru(hra):
    """Vypíše hru textově.

    Tato funkce je jen pro zobrazení, používá proto přímo funkci print()
    a nic nevrací.
    """
    print()
    print('  U     V           W     X     Y     Z')
    print('{} {}       {} {} {} {}'.format(
        popis_vrchni_kartu(hra['U']),
        popis_vrchni_kartu(hra['V']),
        popis_vrchni_kartu(hra['W']),
        popis_vrchni_kartu(hra['X']),
        popis_vrchni_kartu(hra['Y']),
        popis_vrchni_kartu(hra['Z']),
    ))
    print()
    print('  A     B     C     D     E     F     G')
    vypis_sloupecky([
        hra['A'], hra['B'], hra['C'], hra['D'], hra['E'], hra['F'], hra['G']
    ])
    print()

def karta_pasuje(hra, jmeno_odkud, jmeno_kam):
    cervena = [' ♥', ' ♦']
    cerna = ['♣ ', '♠ ']
    sloupec_kam = hra[jmeno_kam]
    sloupec_odkud = hra[jmeno_odkud]
    hodnota_presun, barva_presun, je_otocena_presun = sloupec_odkud[-1]
    hodnota_vrchni, barva_vrchni, je_otocena_vrchni = sloupec_kam[-1]
    if not hra[jmeno_kam]:
        return True
    elif ((barva_presun in cervena and barva_vrchni in cerna) or (barva_presun in cerna and barva_vrchni in cervena)) and (hodnota_presun + 1) == hodnota_vrchni:
        return True
    else:
        return False


def udelej_tah(hra, jmeno_odkud, jmeno_kam):
    """Udělá tah z jednoho místa na druhé.

    Místa jsou označovány velkými písmeny (např. 'A', 'V' nebo 'X').

    Není-li tah možný, vyhodí ValueError s popisem problému.
    """
    
    sloupec_kam = hra[jmeno_kam]
    sloupec_odkud = hra[jmeno_odkud]
    cervena = [' ♥', ' ♦', 'Sr', 'Ka']
    cerna = ['♣ ', '♠ ', 'Kr', 'Pi']
    

    if jmeno_odkud == "U" and jmeno_kam == "V":
        if sloupec_odkud:
            hra = presun_kartu(sloupec_odkud, sloupec_kam, True)
            return hra
        else:
            raise ValueError("Balíček U je prázdný!") 
    elif jmeno_odkud == "V" and jmeno_kam == "U":
        if not sloupec_kam:
            for i in range(len(sloupec_odkud)):
                hra = presun_kartu(sloupec_odkud, sloupec_kam, False)
          
            return hra   
        else:
            raise ValueError("Balíček U není prázdný!")
    elif jmeno_odkud in ['V', 'A', 'B', 'C', 'D', 'E', 'F', 'G'] and jmeno_kam in ['W', 'X', 'Y','Z']:
        hodnota_presun, barva_presun, je_otocena_presun = sloupec_odkud[-1]
        if not sloupec_kam:   
            if hodnota_presun == 1:
                hra = presun_kartu(sloupec_odkud, sloupec_kam, True)
            else:
                raise ValueError("Karta musí být eso")    
        else:
            hodnota_vrchni, barva_vrchni, je_otocena_vrchni = sloupec_kam[-1]
            if barva_presun == barva_vrchni and hodnota_presun == (hodnota_vrchni + 1):
                hra = presun_kartu(sloupec_odkud, sloupec_kam, True)
            else:
                raise ValueError("Přesouvaná karta musí mít stejnou barvu jako cílová a o 1 vyšší hodnotu")
        
        if sloupec_odkud:
            posledni_karta = sloupec_odkud.pop()
            nova_karta = otoc_kartu(posledni_karta, True)
            hra = sloupec_odkud.append(nova_karta)
        return hra
   
    elif jmeno_odkud == "V" and jmeno_kam in ['A', 'B', 'C', 'D', 'E', 'F', 'G']: 
        hodnota_presun, barva_presun, je_otocena_presun = sloupec_odkud[-1]
        if not sloupec_kam:
            if hodnota_presun == 13:
                hra = presun_kartu(sloupec_odkud, sloupec_kam, True)
                return hra
            else: 
                raise ValueError ("Karta musí být král")
        else:
            hodnota_vrchni, barva_vrchni, je_otocena_vrchni = sloupec_kam[-1]
            if ((barva_presun in cervena and barva_vrchni in cerna) or (barva_presun in cerna and barva_vrchni in cervena)) and (hodnota_presun + 1) == hodnota_vrchni:
                presun_kartu(sloupec_odkud, sloupec_kam, True)
                return hra
            else:
                raise ValueError("Přesouvaná karta musí mít jinou barvu než cílová a o 1 nižší hodnotu")
    elif jmeno_odkud in ['A', 'B', 'C', 'D', 'E', 'F', 'G'] and jmeno_kam in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        hodnota_presun, barva_presun, je_otocena_presun = sloupec_odkud[-1]
        
        if jmeno_odkud == jmeno_kam:
            raise ValueError("Zadal jsi stejné sloupečky")

        elif not sloupec_kam:
            # prvni_presouvana_karta = sloupec_odkud[-1]  
                for karta in sloupec_odkud:
                    hodnota, barva, je_otocena = karta
                    if hodnota == 13 and je_otocena == True:
                       
                        poradi = int(sloupec_odkud.index(karta))
                        seznam_presouvanych_karet = sloupec_odkud[poradi: ]
                        pocet = len(seznam_presouvanych_karet)
                        hra = presun_nekolik_karet(sloupec_odkud, sloupec_kam, pocet)
            
        else:    
            hodnota_vrchni, barva_vrchni, je_otocena_vrchni = sloupec_kam[-1]
            for karta in sloupec_odkud:
                hodnota, barva, je_otocena = karta
                if ((barva in cervena and barva_vrchni in cerna) or (barva in cerna and barva_vrchni in cervena)) and (hodnota + 1) == hodnota_vrchni and je_otocena == True:
                    prvni_presouvana_karta = karta
            poradi = int(sloupec_odkud.index(prvni_presouvana_karta))
            seznam_presouvanych_karet = sloupec_odkud[poradi: ]
            pocet = len(seznam_presouvanych_karet)
            hra = presun_nekolik_karet(sloupec_odkud, sloupec_kam, pocet)
        
        if sloupec_odkud:
            posledni_karta = sloupec_odkud.pop()
            nova_karta = otoc_kartu(posledni_karta, True)
            hra = sloupec_odkud.append(nova_karta)
        return hra  
