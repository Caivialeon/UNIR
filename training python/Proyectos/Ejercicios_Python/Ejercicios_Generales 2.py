#Pedir numeros al usuario hasta que introduzca uno negativo.
#Al finalizar mostrar la cantidcad de numeros introducidos sin contar el negativo.


numeros = []
num1=0
contador = 0
while num1>=0:
    num1 = int(input("Escribe el numero a ingresar : "))
    numeros.append(num1)
    if num1>=0:
        contador = contador +1
else:
    numeros.pop()
print(f"Han sido un total de {contador} de numeros")
print(f"los numeros introducidos son: {numeros}")

