def triangulo(numero):
    if numero%2 != 0 or numero%2 ==0:
        base = '*' * numero
        base1= '-' *numero
        medio= int(numero/2)-1
        espacio = int((numero-1)/2)
        for impar in range(1, numero, 2):
            imparstr = '*'*impar
            print('\033[1;32m'+' ' * espacio +imparstr)
            espacio = espacio - 1
        print('\033[1;32m'+base)

    return
triangulo(12)

#for i in range(1, 6, 2):
 #   print(i)