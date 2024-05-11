#Este codigo nos determina si una frase es un palindromo o no!

#frase = "Anita lava la tina"
frase= input("Digite el palindromo: ")
frase_min= list(frase.lower())
sin_espacio= []
for string in frase_min:
    if string != '' and string != ' ':
        sin_espacio.append(string)
#print (sin_espacio)
rev = sin_espacio[::-1]
#print(rev)
if sin_espacio == rev:
    print('True')
else:
    print('False')