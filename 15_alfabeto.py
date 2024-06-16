def alfabeto(cadena):
    alfabeto =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cadena = cadena.lower()
    ordenado=[]
    palabra =cadena
    for posicion, letra in enumerate(alfabeto):
        #print(letra)
        for e in cadena:
            if e == letra:
                print(letra)
                ordenado.append(letra)
    print(ordenado,'***********  ')
    return

alfabeto('hola')