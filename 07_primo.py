#Este codigo nos indica si un numero es primo
import math
from datetime import datetime

def primo (numero):
    if numero<=1:
        return 'El numero no es primo'
    #numero = 13
    redondear = math.ceil(numero/2)
    for i in range(2,redondear):
        #print(i)
        if numero%i == 0:
            return 'El numero: '+str(numero)+' no es primo'
        if i==redondear-1:
            return 'El numero: '+str(numero)+' es primo'

print(primo(10226077))

""" 
hora_antes = datetime.now()
hora_despues = datetime.now()
hora_total = hora_despues-hora_antes
print(str(hora_total),'<----------------- diferencia')
 """
