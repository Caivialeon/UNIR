#4.- Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Operaciones:
    def __init__(self):
        self.num1 = float(input("Dame el primer valor : "))
        self.num2 = float(input("Dame el segundo valor : "))
        self.res = 0

    def suma(self):
        self.res = self.num1 + self.num2
        print(f"El resultado de la suma es {self.res}")

    def resta (self):
        self.res = self.num1 - self.num2
        print(f"El resultado de la resta es {self.res}")

    def division(self):
        self.res = self.num1 / self.num2
        print(f"El resultado de la division es {self.res}")

    def multiplicacion(self):
        self.res = self.num1 * self.num2
        print(f"El resultado de la multiplicacion es {self.res}")

op = Operaciones()

op.suma()
op.resta()
op.multiplicacion()
op.division()

'''
# creamos la clase
class Calculadora:
	# iniciamos con el método __init__
	def __init__(self):
		self.valor1=int(input("Ingrese el primer valor: "))
		self.valor2=int(input("Ingrese el segundo valor: "))
 
	# función para sumar
	def suma(self):
		suma=self.valor1+self.valor2
		print("El resultado de la suma de los valores es: ",suma)
 
	# función para restar
	def resta(self):
		resta=self.valor1-self.valor2
		print("El resultado de la resta de los valores es: ",resta)
 
	# función para calcular el producto
	def multiplicacion(self):
		pro=self.valor1*self.valor2
		print("El resultado de la multiplicación de los valores es: ",pro)
 
	# función para dividir
	def division(self):
		div=self.valor1/self.valor2
		print("El resultado de la división de los valores es: ",div)
 
	# función para imprimir
	def imprimir(self):
		print("Los valores son: ")
		print("Valor 1: ",self.valor1)
		print("Valor 2: ",self.valor2)
 
 
# bloque principal
calcular=Calculadora()
calcular.imprimir()
calcular.suma()
calcular.resta()
calcular.multiplicacion()
calcular.division()
'''

