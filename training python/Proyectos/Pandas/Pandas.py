import pandas as pd
import numpy as np

serie = pd.Series([1,2,4,5,6] , index = ["a","b","c","d","e"])
print(serie)

diccionario = {"a":5, "b":6,"c":89 ,"d":97, "e" : 15}
serie1 = pd.Series(diccionario)
print(serie1)

print(serie1.index)
print(serie1.values)

resultado = serie1+serie
print(resultado)
resultado = serie1*10
print(resultado)

#dataframes

dic1 = {"columna 1" : pd.Series([1,2,4,5,6] , index = ["a","b","c","d","e"]) , "columna 2": pd.Series([8,9,10,11,12] , index = ["a","b","c","d","e"])}

dataframe = pd.DataFrame(dic1)

print(dataframe)

lista = [{"a":1 , "b":5, "c": 7} , {"c":1 , "h":5, "b": 7}]

dataframe1 = pd.DataFrame(lista)
print(dataframe1)

print(dataframe1["b"])

#agregar columna al dataframe de

dataframe1["t"] = pd.Series([5,2], index = [0,1])
print(dataframe1)

dataframe["columna 3"] = pd.Series([1,2,4,5,6] , index = ["a","b","c","d","e"])
print(dataframe)

#borrar columna del data frame

del dataframe["columna 1"]
print(dataframe)

filtro = np.array([True,False,True,False,True])

print(dataframe[filtro])
print(dataframe.T)

pd.read_csv(dataframe)