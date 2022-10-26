#Clases .- contenedor donde vamos a almacenar objetos.
'''class Auto:  marca = ""  modelo = 2004  placa = ""  taxi = Auto()  print(taxi.modelo)
'''
#Clases y objetos II

class persona:
    '''objeto y atributos de la clase'''
    doctor = "Aldo"
persona.doctor

class jugadores_A:
    j1 = "Messi"
    j2 = "Ronaldo"
#print(jugadores_A.j1 , jugadores_B.j2)

class jugadores_B:
    j3 = "Marcelo"
    j1 = "Falcao"
#print(jugadores_B.j1)

class nombre:
    pass
aldo = nombre()
angelica = nombre()

#objeto.atributo = valor

aldo.edad = 30
aldo.sexo = "Masculino"
aldo.pais = "Mexico"
angelica.edad = 33
angelica.sexo = "Femenino"
angelica.pais = "Mexico"

print(aldo.edad)
print(angelica.edad)
