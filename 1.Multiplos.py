
#Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:


numero = int(input("Ingrese un numero: "))
for i in range(10):
    print(f"{numero} x {i+1} = {numero*(i+1)}")