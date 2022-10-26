#Funcion super se usa para llamar metodos definidos, en herencia multiple

class Mamifero:
    def __init__(nombre,self):
        print(nombre," es un animal de sangre caliente")

class Leon(Mamifero):
    def __init__(self):
        print("el leon es un animal de cuatro patas")
        super().__init__("simba")
        #Mamifero.__init__(self,"Simba")

nuevo_leon = Leon()


