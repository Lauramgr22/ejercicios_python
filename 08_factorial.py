#Este codigo halla el factorial de un numero

def factorial(numero):
    resultado =1
    if numero==1 and numero==0:
        return 'El factorial de: '+str(numero)+' es: 1'
    for i in range(1,numero+1):
        #print(i)
        resultado= resultado*i
    return 'El factorial de: '+str(numero)+' es: '+str(resultado)

print(factorial(0))
print(factorial(10))
print(factorial(5))