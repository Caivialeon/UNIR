#Polimorfismo por funcion
class Tomate:
    def tipo(self):
        print("vegetal")

    def color(self):
        print("rojo")

class Manzana:
    def tipo(self):
        print("fruta")

    def color(self):
        print("verde")

def funcion(objeto):
    objeto.tipo()
    objeto.color()

nuevo_tomate = Tomate()
funcion(nuevo_tomate)
nueva_manzana = Manzana()
funcion(nueva_manzana)

#Polimorfismo con metodos, funciona cuando tenemos varias clases

class Colombia:
    def capital(self):
        print("Bogota")

    def idioma(self):
        print("Español")

class Francia:
    def capital(self):
        print("Paris")

    def idioma(self):
        print("Frances")

colombiano = Colombia()
frances = Francia()

for pais in (colombiano,frances):
    pais.capital()
    pais.idioma()
#polimorfismo por herencia

class Aves:
    def volar(self):
        print("la mayoria de las aves pueden volar")

class Aguila(Aves):
    def volar(self):
        print("el aguila si puede volar")

class Gallina(Aves):
    def volar(self):
        print("la gallina no puede volar")

obj_ave = Aves()
obj_aguila = Aguila()
obj_gallina = Gallina()
obj_ave.volar()
obj_aguila.volar()
obj_gallina.volar()