#Este codigo halla los numeros triangulares dada su fila

def triangular(numero):
    resultado =0
    if numero<1:
        return 'Numero no valido'
    for i in range(1,numero+1):
        #print(i)
        resultado= resultado+i
    return 'El numero triangular de: '+str(numero)+' es: '+str(resultado)

print(triangular(3))
print(triangular(5))
print(triangular(7))