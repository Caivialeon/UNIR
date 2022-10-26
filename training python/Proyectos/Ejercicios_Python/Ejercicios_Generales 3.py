#Pedir un numero por teclado y mostrar
# los 10 primeros terminos de su tabla de multiplicar.

def operacion(numero):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

num = int(input("Escribe el numero a mostrar : "))
operacion(num)


'''
num = int(input("Escribe el numero a mostrar : "))
for i in range(0,11):
    acum = i*num
    print(f"{num} x {i} = {acum}")
'''
