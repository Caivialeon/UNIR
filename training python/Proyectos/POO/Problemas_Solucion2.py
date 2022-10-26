#2.- Realizar un programa que tenga una clase Persona con las siguientes características. La clase tendrá como atributos el nombre y la edad de una persona. Implementar los métodos necesarios para inicializar los atributos, mostrar los datos e indicar si la persona es mayor de edad o no.

class Persona:

    def inicializar (self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar (self):
        if self.edad <= 18:
            print(f"{self.nombre} no es mayor de edad")
        else:
            print(f"{self.nombre} si es mayor de edad")

prs1 = Persona()
prs2 = Persona()

prs1.inicializar("Carlos",15)
prs2.inicializar("Aldo",34)

prs1.mostrar()
prs2.mostrar()
