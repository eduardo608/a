#Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos. Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.

num1= int(input("Ingrese num: "))
num2= int(input("Ingrese num: "))
suma=0
for i in range(num1+1,num2):
    suma += i
print(f"La suma es {suma}")