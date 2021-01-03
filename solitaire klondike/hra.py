from klondike import udelej_hru, vypis_hru, presun_kartu, presun_nekolik_karet
from karty import otoc_kartu, popis_kartu

def nacti_tah():
    while True:
        tah = input('Tah? ')
        try:
            jmeno_zdroje, jmeno_cile = tah.upper()
        except ValueError:
            print('Tah zadávej jako dvě písmenka, např. UV')
        else:
            return jmeno_zdroje, jmeno_cile

def hrac_vyhral(hra):
    """Vrací True, pokud je hra vyhraná.
    """
    if len(hra['W']) + len(hra['X']) + len(hra['Y']) + len(hra['Z']) == 52:
        return True
    else:
        return False

































print()

hra = udelej_hru()

while not hrac_vyhral(hra):
    vypis_hru(hra)
    odkud, kam = nacti_tah()
    try:
        udelej_tah(hra, odkud, kam)
    except ValueError as e:
        print('Něco je špatně:', e)

vypis_hru(hra)
print('Gratuluji!')