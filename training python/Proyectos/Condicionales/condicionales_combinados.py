#condicionales combinados

edad = int(input("Dame tu edad : "))

if edad > 0 and edad < 100:
    '''0<edad<100'''
    print("edad correcta")
    if edad>=18:
        print("es mayor de edad")
    else:
        print("no es mayor de edad")
else:
    print("edad incorrecta")

'''edad>=18:
print("es mayor de edad")
else:
print("no es mayor de edad")'''