#Este codigo realiza la conversion de horario de 12horas a 24horas

#hora = 3
#minutos = 15
#formato = "PM"

hora= int(input("Digite la hora: "))
minutos= int(input("Digite los minutos: "))
formato= input("Digite el formato: ").upper()
if formato == "AM" and hora<= 12:
    print("la hora es=", str(hora), ":",str(minutos)," ",formato)
else:
    print("Esta mal ingresado el valor de la hora")
if formato == "PM":
    hora = hora + 12
    print("la hora es=", str(hora), ":", str(minutos), " ", formato)
