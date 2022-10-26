#Pedir 10 numeros por teclado. Sumarlos y
#mostar el resultado en pantalla

def sumatoria (n):
    numtotal = 0
    for i in range(0, n):
        num1 = float(input("Dame el numero : "))
        numtotal = num1 + numtotal
    return numtotal

i = int(input("indique cuantos numeros va a sumar : "))
total = sumatoria(i)
print(f"el resultado de la suma total es : {total}")

'''
numtotal = 0
for i in range(0,10):
    num1= float(input("Dame el numero : "))
    numtotal = num1 + numtotal
print(f"la suma total es : {numtotal}")

'''