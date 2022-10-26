#3.- Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno).

class Triangulo ():
    def datos(self):
        self.a = float(input("Dame el primer valor : "))
        self.b = float(input("Dame el segundo valor : "))
        self.c = float(input("Dame el tercer valor : "))

    def mayor (self):
        if self.a >= self.b and self.a >= self.c :
            print(f"el mayor es : {self.a}")
        elif self.b >= self.c and self.b >= self.a:
            print(f"el mayor es : {self.b}")
        elif self.c >= self.b and self.c >= self.a:
            print(f"el mayor es : {self.c}")

    def tipo (self):
        if self.a ==self.b and self.b == self.c:
            print("es un triangulo Equilatero")
        elif self.a != self.b and self.a != self.c:
            print("es un triangulo Escaleno")
        else:
            print("es un triangulo isoceles")

trg = Triangulo()

trg.datos()
trg.mayor()
trg.tipo()

'''
# creamos nuestra clase
class Triangulo:
	# inicializamos
	def inicializar(self):
		self.lado1=int(input("Ingrese el valor del primer lado: "))
		self.lado2=int(input("Ingrese el valor del segundo lado: "))
		self.lado3=int(input("Ingrese el valor del tercer lado: "))
 
	# imprimimos 
	def imprimir(self):
		print("Los lados del triángulo tienen el valor de")
		print("Lado 1: ",self.lado1)
		print("Lado 2: ",self.lado2)
		print("Lado 3: ",self.lado3)
 
	# comprobamos el lado mayor
	def mayor(self):
		print("El lado mayor es")
		if self.lado1>self.lado2 and self.lado1>self.lado3:
			print("Lado 1: ",self.lado1)
		elif self.lado2>self.lado3:
			print("Lado 2: ",self.lado2)
		else:
			print("Lado 3: ",self.lado3)
 
	# comprobamos el tipo de triángulo
	# equilátero -> todos los lados iguales
	# isósceles -> dos lados iguales
	# escaleno -> todos los lados desiguales
	def tipo(self):
		if self.lado1==self.lado2 and self.lado1==self.lado3:
			print("Es un triángulo equilátero")
		elif self.lado1!=self.lado2 and self.lado1!=self.lado3:
			print("Es un triángulo escaleno")
		else:
			print("Es un triángulo isósceles")
 
# bloque principal
figura=Triangulo()
figura.inicializar()
figura.imprimir()
figura.mayor()
figura.tipo()
'''