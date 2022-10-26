#f-strings
#format %
'''
curso = "python"
print("tutoriales de %s"%curso)

nombre = "aldo"
edad = 25

print("soy %s y tengo %s años."%(nombre ,edad))
print("que tal soy {} y mi edad es {} años".format(nombre,edad))
print(f"hola soy {nombre} y cumplo {edad} años")
'''

class Estudiante:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
#def __str__ es la representacion informal de una cadena o un objeto , se regresa un string
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad}"

nuevo_estudiante = Estudiante("aldo","bernal",34)
print(f"{nuevo_estudiante}")

