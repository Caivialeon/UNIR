#Map ejecuta una funcion especifica para cada elemento iterable
#Filter crea un nuevo iterador a partir de un iterable existente



def mult(n):
    return n * 5

lista = [1,2,3,4,5,6,7]

lista_map = list(map(mult,lista))
print(lista_map)

def cursos(c):
    return c.upper()

tupla = ("php", "python" , "java", "dart", "css")
tupla_map = tuple(map(cursos,tupla))
print(tupla_map)

def impares(n):
    if(n%2==1):
        return n

lista = [1,2,3,4,5]

lista_impares = list(filter(impares,lista))
print(lista_impares)

