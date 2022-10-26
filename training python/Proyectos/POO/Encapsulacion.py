#Encapsulacion .- ocultamiento de datos del estado interno.

class Cliente:
#encapsulamiento de variable
    def __init__(self):
        self.__codigo = 4321
    def __cuenta(self):
        print("cuenta de procesamiento")
#obtener datos de la variable encapsulada con get
    def getcodigo(self):
        return  self.__codigo
'''
persona = Cliente()
print(persona.__codigo)
'''

persona = Cliente()
#objeto._nombreclase_nombre atributo
print(persona._Cliente__codigo)
persona._Cliente__cuenta()
