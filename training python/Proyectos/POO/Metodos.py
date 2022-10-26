#Metodos .- es una funcion dentro de una clase.
#Class nombre de la clase:     Def nombre del metodo
#self hace referencia a un objeto
#_init_(self) es un constructor

class Matematica:
    def suma(self):
        self.n1 = 2
        self.n2 = 3
s = Matematica()
s.suma()
#print(s.n1 + s.n2)
#Metodos

class Ropa:
    def __init__(self):
        self.marca = "willow"
        self.talla = "M"
        self.color = "rojo"

camisa = Ropa()
#print(camisa.talla)
#print(camisa.marca)

#se crea la clase
class Calculadora :
    #se crea el metodo
    def __init__(self,n1,n2):
        self.suma = n1+n2
        self.resta = n1-n2
        self.producto = n1*n2
        self.division = n1/n2
#se crea el objeto con los parametros
operacion = Calculadora (2,3)
print(operacion.suma)

