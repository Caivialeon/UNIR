#Diccionarios

#diccionario = {"clave":"valor"}
'''
diccionario = {"nombre":"Aldo","edad":23}
print(diccionario["nombre"])
print(diccionario["edad"])

datos_personales = {"Pais":"Mexico","Ciudad":"CDMX"}
datos_personales["Ciudad"] = "Estado de Mexico"

print(datos_personales["Ciudad"])
#añade un nuevo valor al diccionario
dict = {"Aldo":34,"Angelica":37,"Sonia":53,"Gaby":25}
dict.update({"Alberto":63})
print(dict)
#borrar valor del diccionario
del dict ["Angelica"]
print(dict)
'''
#combinar diccionario con lista
dict = {"Aldo":34,"Angelica":37,"Sonia":53,"Gaby":25}
varones = {"Aldo":34}
mujeres = {"Angelica":37,"Sonia":53,"Gaby":25}
estudiantes = list(dict.keys())
estudiantes.sort()

for e in estudiantes:
    print(" : ".join((e,str(dict[e]))))






