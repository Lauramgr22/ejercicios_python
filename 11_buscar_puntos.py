def buscar(cadena):

    for posicion, simbolo in enumerate(cadena):
        if posicion+1 == len(cadena):
            break
        if cadena[posicion+1] =='*' and simbolo=='.' and cadena[posicion-1]=='*':
             print(posicion-1,posicion,posicion+1)
    print("----------------")

    return

buscar('***..**...**.*') # 3 4,  7 8,  8 9
buscar('*.*.*.********') #
buscar('..............') # 0 1, 1 2, 2 3, 3 4, 4 5, 5 6, 6 7, 7 8, 8 9, 9 10, 10 11, 11 12, 12 13
buscar('..**..***.*..') #  0 1, 4 5, 11 12