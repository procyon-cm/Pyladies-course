def tah(pole, pozice, symbol):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici

    `pole` je herní pole, na které se hraje.
    `pozice` je číslo políčka. Čísluje se od nuly.
    `symbol` může být 'x' nebo 'o', podle toho jestli je tah za křížky
    nebo za kolečka.
    """
    nove_pole = pole[:pozice] + symbol + pole[(pozice + 1):]
    
    if pozice < 0 or pozice > 19:
        raise ValueError
    elif symbol != "x" and symbol != "o":
        raise ValueError
    elif pole[pozice] != "-":
        raise ValueError
    else:
        return nove_pole

