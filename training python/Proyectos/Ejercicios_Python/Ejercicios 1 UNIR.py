

def ejercicio_2(precio):
    precio_total  = (precio*.21) + precio
    return precio_total

def ejercicio_3(diametro):
    area  =  ((diametro/2)**2) * 3.1415
    return area

def ejercicio_4(n, m):
    resto = n % m
    cociente = n // m
    return cociente, resto

def ejercicio_1(dni):
    # Escribe aquí el código del ejercicio
    dni = int(dni)
    diccionario = {0:"T",1:"R",2:"W",3:"A",4:"G",5:"M",6:"Y",7:"F",8:"P",9:"D",10:"X",11:"B",12:"N",13:"J",14:"Z",15:"S",16:"Q",17:"V",18:"H",19:"L",20:"C",21:"K",22:"E" }
    letra = str(diccionario[dni]).upper()
    return letra

n = int(input("dame el numero"))
print(ejercicio_1(n))


'''
n = float( input("dame el numero"))
m = float(input("dame el otro numero"))

resto = n % m
cociente = n // m

print(resto , "  ", cociente)
'''
