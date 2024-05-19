#Este codigo retorna una cadena de texto en formato slug

frase = 'TEXto% con caracteres$# especial-es 6 9!!!'
frase = frase.replace('%','').replace('$','').replace('#','').replace('-','').replace('!','').lower()
frase = frase.replace(' ','-')
print(frase)