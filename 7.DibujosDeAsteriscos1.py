#Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:



Alt = int(input("Altura:"))
Ancho = int(input("Ancho: "))

for i in range(Alt):
    for j in range(Ancho):
        print("*", end="")
    print()