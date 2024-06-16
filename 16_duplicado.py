from collections import Counter
def duplicado(cadena):
    contador = Counter(cadena)
    conjunto = set(cadena)
    lista = list(conjunto)
    contador1 = Counter(lista)
    res= contador-contador1
    StrPalabra = ", ".join(res)
    print(StrPalabra)
    return

duplicado(['Juan','Camilo','Juan','Andres','Santigo','Camilo'])