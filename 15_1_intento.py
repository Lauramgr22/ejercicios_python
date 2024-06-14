def alfabeto(cadena):
    alfabeto =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cadena = cadena.lower()
    palabra =[]
    for e in cadena:
        for posicion, letra in enumerate(alfabeto):
            if e == letra:
                palabra.append(alfabeto[posicion+1])
                #print(alfabeto[posicion+1])
    StrPalabra = "".join(palabra)
    print(StrPalabra)
    return

alfabeto('hola mundo')
alfabeto('MUNDO')
alfabeto('yorro')
