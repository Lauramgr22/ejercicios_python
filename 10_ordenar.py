#Este codigo ordena una lista de numeros

def ordenar(lista):
    aux = [];
    for posicion, valor in enumerate(lista):
        #print(lista[posicion])
        if lista[posicion]>lista[posicion+1] and posicion+1 == len(lista):
            aux.append(lista[posicion])
    print(aux)
    return

print(ordenar([4, 3, 1, 6]))
#print(4[0]>3[1])