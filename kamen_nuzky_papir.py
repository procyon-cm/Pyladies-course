def hra():
    from random import randrange
    cislo = randrange(2)

    if cislo == 0:
        tah_pocitace = "kámen"
    elif cislo == 1:
        tah_pocitace = "nůžky"
    else:
        tah_pocitace = "papír"

    tah_hrace = input("Jaký je váš tah? ")

    if tah_hrace != "konec":
        if tah_hrace == "kámen":
            if tah_pocitace == "kámen":
                print("Remíza!")
                hra()
            elif tah_pocitace == "nůžky":
                print("Vyhrál jsi!")
                hra()
            else:
                print("Prohrál jsi!")
                hra()
        elif tah_hrace == "nůžky":
            if tah_pocitace == "kámen":
                print("Prohrál jsi!")
                hra()
            elif tah_pocitace == "nůžky":
                print("Remíza!")
                hra()
            else:
                print("Vyhrál jsi!")
                hra()
        elif tah_hrace == "papír":
            if tah_pocitace == "kámen":
                print("Vyhrál jsi!")
                hra()
            elif tah_pocitace == "nůžky":
                print("Prohrál jsi!")
                hra()
            else:
                print("Remíza!")
                hra()      
        else:
            print("Omlouvám se, znám jen tři slova - kámen, nůžky, papír.")
            hra()

    else:    
        print("Konec hry")

hra()