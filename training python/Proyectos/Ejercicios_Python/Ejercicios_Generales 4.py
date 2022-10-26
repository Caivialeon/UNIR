#Pedir dos numeros por teclado y mostrar todos
#los numeros pares comprendidos entre ambos.
n=0
n2=0

n =  int(input("Escribe el primer numero : "))
n2 = int(input("Escribe el segundo numero : "))
while n >= n2:
    n2 = int(input("Escribe el segundo numero : "))
for n in range(n,n2):
    if n%2 == 0 :
        print(n)
        n = n + 1

