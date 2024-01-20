
#Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:

LongLat=int(input("Lado: "))
LongFinal = LongLat + 2*(LongLat-1)
for i in range(LongLat):
    cadena=""
    for j in range(LongLat+2*i):
        cadena+="*"
    print(cadena.center(LongFinal))
for x in range(1,LongLat):
    cadena=""
    for j in range(2,LongLat+2*(LongLat-x),1):
        cadena+="*"
    print(cadena.center(LongFinal))
