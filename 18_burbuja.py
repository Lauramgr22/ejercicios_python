import time
lista = [7, 6, 3, 2, 5, 1, 4]
posicion = 0

while True:
    aux = 0
    posicion += 1

    if posicion == len(lista):
        posicion = 1

    if lista[posicion] < lista[posicion - 1]:
        aux = lista[posicion]
        lista[posicion] = lista[posicion - 1]
        lista[posicion - 1] = aux
    print(lista)
    time.sleep(0.5)



