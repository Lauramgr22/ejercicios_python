#Este codigo nos determina la primera letra que se repite o no!

#frase = "Hello word"
frase= input("Digite la palabra: ")
frase = frase.lower().replace(' ','')
letras = []
for letra in frase:
    #print(letra)
    if letra in letras:
        print("la primera letra repetiva es: ", letra)
        break
    else:
        letras.append(letra)
if letras == list(frase):
    print("None")
#print(letras)

