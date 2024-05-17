#Este codigo nos determina si dos palabras son un anagrama o no!

#palabra1 = "Mora"
#palabra2= "Roma"
palabra1= input("Digite la palabra 1: ")
palabra2= input("Digite la palabra 2: ")

palabra1= set(palabra1.lower())
palabra2= set(palabra2.lower())
if palabra1 == palabra2:
    print('True')
else:
    print('False')