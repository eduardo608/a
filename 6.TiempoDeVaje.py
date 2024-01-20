#Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.


tiempo = int(input("Duracion tramo: "))
total=0
while tiempo!=0:
    total+=tiempo
    tiempo = int(input("Duracion tramo: "))
print(f"Tiempo total de viaje: {total//60}:{str(total%60).zfill(2)} horas")
