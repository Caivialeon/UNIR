#ejercicio 1

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: "))


if num1%2 == 0 and num2%2==0:
    print("Ambos son pares")
elif num1%2 ==0 and num2%2 !=0:
    print(f"{num1} es par")
elif num1%2 !=0 and num2%2==0:
    print(f"{num2} es par")
else:
    print("ambos son impares")