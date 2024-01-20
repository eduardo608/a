#Escriba un programa que entregue todos los divisores del número entero ingresado:

num = int(input('ingrese un numero'))

for i in range(1, num + 1):
    if num%i == 0:
        print(i, end=' ')