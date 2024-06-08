def buscar(cadena):

    for posicion, simbolo in enumerate(cadena):
        if posicion+2 == len(cadena):
            break
        if cadena[posicion+2]=='-' and cadena[posicion+1] =='*' and simbolo=='.' and cadena[posicion-1]=='-' and cadena[posicion-2]=='-':
            if posicion-2>=0 and posicion-1>=0:
                print(posicion - 2, posicion - 1, posicion, posicion + 1, posicion + 2)
    print("----------------")

    return

buscar('--.*-') #
buscar('-.*.*.*--.****') #
buscar('--.*-.--.*-..--.*-') #
buscar('-.*--') #