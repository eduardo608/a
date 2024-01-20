#Escriba un programa que muestre una tabla de multiplicar como la siguiente:

filas = 10
columnas = 10

for i in range(1, filas + 1):
     for j in range(1, columnas + 1):
        mult = i * j
        print(f"{mult:4}", end="")
     print() 
