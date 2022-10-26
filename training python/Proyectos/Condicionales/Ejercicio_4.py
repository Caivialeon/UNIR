#Ejercicio 4

num1 = float(input("digite un numero: "))
num2 = float(input("digite un numero: "))

operacion = input("Digite la operacion a realizar : ")

if operacion == 's' or operacion == 'S':
    print("se realizara una suma")
    resultado = num1 + num2
    print(f"el resultado es : {resultado}")
elif operacion == 'R' or operacion == 'r':
    print("se realizara una resta")
    resultado = num1 - num2
    print(f"el resultado es : {resultado}")
elif operacion == 'p' or operacion == 'P' or operacion == 'M' or operacion =='m':
    print("se realizara una multiplicacion")
    resultado = num1 * num2
    print(f"el resultado es : {resultado}")
elif operacion == 'D' or operacion == 'd':
    print("se realizara una division")
    resultado = num1 / num2
    print(f"el resultado es : {resultado:.2f}")
else:
    print("dato incorrecto")