#Se refiere a la posibilidad de crear una clase a partir de multiples clases superiores
#herencia multinivel .- las caracteristicas de la clase base y la clase derivada se heredan en la nueva
#clase derivada


class Telefono:

    def __init__(self):
        pass

    def llamar(self):
        print("llamando...")

    def contestar(self):
        print("ocupado...")

class Camara:

    def __init__(self):
        pass

    def fotografia(self):
        print("tomando fotos...")

class Reproduccion:

    def __init__(self):
        pass

    def reproducciondemusica(self):
        print("reproduciondo musica...")

    def reproducirvideo(self):
        print("reproduciendo video...")

class Smartphone(Telefono,Camara,Reproduccion):
#metodo __del__ es para limpiar recursos
    def __del__(self):
        print("telefono apagado")

movil = Smartphone()

print(movil.llamar())



