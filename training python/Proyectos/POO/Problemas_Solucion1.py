#1.- Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.´

class Alumno:
#iniciamos los atributos

#funcion para obtener los datos
    def alumno_datos (self):
        self.nombre = str(input("dame el nombre del alumno : "))
        self.calificacion = float(input("dame la calificacion del alumno : "))
#funcion para imprimir los datos
    def alumno_imprimir(self):
        if self.calificacion >=8:
            print(f"El alumno {self.nombre} ha aprobado con una calificacion de {self.calificacion}")
        else:
            print(f"El alumno {self.nombre} ha reprobado con una calificacion de {self.calificacion}")
#creamos los objetos de la clase
alum = Alumno()
#imprimimos resultados.
alum.alumno_datos()
alum.alumno_imprimir()

'''
# inicializamos la clase
class Alumno:
    # inicializamos los atributos
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
 
    # función para imprimir los datos
    def imprimir(self):
               print("Nombre: ",self.nombre)
               print("Nota: ",self.nota)
               
    # función para obtener el resultado
    def resultado(self):
               if self.nota < 5:
                              print("El alumno ha suspendido")
               else:
                              print("El alumno ha aprobado")
 
# bloque principal
# creamos los nuevos objetos
alumno1=Alumno()
alumno2=Alumno()
 
# inicializamos los atributos
alumno1.inicializar("ivan",8)
alumno2.inicializar("juan",4)
 
# imprimimos los datos y resultados de cada alumno
alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()

'''