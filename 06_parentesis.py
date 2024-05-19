#Este codigo nos demuestra se tenemos parentesis balanceados o desbalanceados

parentesis= list('()()()()()')
#print(parentesis)
menos = 0
contador = 0
for letra in parentesis:
    if letra in '(':
        contador += 1
    if letra in ')':
        menos += 1
#print(contador,'----------')
#print(menos, '*******')

if menos == contador and menos!=0:
    print('True')
else:
    print('False')

