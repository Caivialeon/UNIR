#Ejercicio 5 cajero automatico


saldo = float(1000)

operacion = int(input("\t.:MENU:.\nIngrese la operacion a realizar \n1.Ingresar dinero en la cuenta\n2.retirar dinero de la cuenta\n3.mostrar dinero disponible\n4.salir\n"))

if operacion == 1:
    dinero = float(input("ingrese el dinero : "))
    saldo = saldo + dinero
elif operacion ==2:
    dinero = float(input("dinero a retirar"))
    if dinero>saldo:
        print("No tiene suficiente dinero para retirar esa cantidad")
    else:
        saldo = saldo - dinero
elif operacion== 3:
    print(f"El saldo es de : {saldo}")
elif operacion == 4:
    print("Hasta luego")
else:
    print("Opcion no valida")


