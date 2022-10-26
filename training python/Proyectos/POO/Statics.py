'''
Definiciones:

Clase .- una clase es como una plantilla para crear objetos.

instancia .- un objeto se crea usando el constructor de una clase. Una vez que el objeto es creado
se le conoce como una instancia de la clase.

Metodo o funcion .- pedazo , parte o fragmento de algoritmo a ejecutar encapsulado.

Metodos estaticos .- no se tiene acceso desde el exterior , por lo que no puede llamar a ningun atributo
                    dentro de clase
    @staticmethod
Metodos clase .-
    @classmethod .- este metodo puede ser llamado sin crear una instancia de la clase
Metodos instancia.

'''
'''
class Pastel:

    def __init__(self,ingredientes):
        self.ingredientes = ingredientes
#regresa elementos string.
    def __repr__(self):
        return f"pastel({self.ingredientes !r})"

    @classmethod
    def pastel_chocolate(cls):
        return cls(["Harina","leche","chocolate"])
    @classmethod
    def pastel_vainilla(cls):
        return cls(["Harina","leche","vainilla"])

print(Pastel.pastel_chocolate())
'''
import math
class Pastel:

    def __init__(self,ingredientes,tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño


    def __repr__(self):
        return (f"Pastel({self.ingredientes0}, "f"{self.tamaño})")

    def area(self):
        return self.tamaño_area(self.tamaño)
    @staticmethod
    def tamaño_area(A):
        return A ** 2 * math.pi

nuevo_pastel = Pastel (["harina","azucar","leche","crema"],4)
print(nuevo_pastel.ingredientes)
print(nuevo_pastel.tamaño)
print(nuevo_pastel.tamaño_area(4))






