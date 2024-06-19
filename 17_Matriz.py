import random
# m= numero de filas; n= numero de columnas; a= valor aletorio 1; b= valor aleatorio 2

def matriz(m,n, a, b):
    total = []; vector = []
    vector.append(a) ; vector.append(b)
    #m = range(m)  ; n = range(n)
    for i in range(m):
        total.append(random.choices(vector))
        for j in range(n):
            total[i].append(random.choice(vector))
    #print(total)
    print('La matriz de dimension ', m, 'x',n,' es: ')
    for f in range(m):
        for c in range(n):
            print(total[f][c], end=' ')
        print()
    return
matriz(5,5, 0, 1)
