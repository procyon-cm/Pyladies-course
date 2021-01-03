pole = str("-" * 20)
symbol = "x"

def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"

from util import tah

def tah_hrace(pole, symbol):
    """Zeptá se hráče na tah a vrátí nové herní pole

    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    """
    
   
    while True:
        try:
            pozice = int(input("Kam chceš hrát? "))
            break
        except ValueError:
            print("Zadávej čísla!")   
      
    if pozice < 0 or pozice > 19  or pole[pozice] != "-":
        print("Tam nejde hrát!")
        return tah_hrace(pole, symbol)     
    else: 
        my_tah = tah(pole, pozice, symbol)
        return my_tah

def tah_hrace(pole, symbol):
    """Zeptá se hráče na tah a vrátí nové herní pole

    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    """
    
   
    while True:
        try:
            pozice = int(input("Kam chceš hrát? "))
            break
        except ValueError:
            print("Zadávej čísla!")   
      
    if pozice < 0 or pozice > 19  or pole[pozice] != "-":
        print("Tam nejde hrát!")
        return tah_hrace(pole, symbol)     
    else: 
        my_tah = tah(pole, pozice, symbol)
        return my_tah
from random import randrange

print(pole)
def piskvorky1d(pole):
 
    pole = tah_hrace(pole, symbol)
    while True:
        
        vysledek = vyhodnot(pole)
        print(pole)
        if vysledek == "Vyhrál jsi!" or vysledek == "Prohrál jsi!" or vysledek == "Remíza!":
            return vysledek
        else:
            pole = tah_pocitace(pole, symbol)
            print(pole)
            vysledek = vyhodnot(pole)
            if vysledek == "Vyhrál jsi!" or vysledek == "Prohrál jsi!" or vysledek == "Remíza!":
                return vysledek
            else: 
                return piskvorky1d(pole)