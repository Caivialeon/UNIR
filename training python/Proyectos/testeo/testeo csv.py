import pandas as pd
import numpy as np
import math

contador = 0
total = 0
ruta  = "titanic.csv"
df = pd.read_csv(ruta)
dataframe = pd.DataFrame(df)
dataframe2 = pd.DataFrame()
#dataframe["Age"] = dataframe["Age"].astype(int)

#dataframe2 = dataframe[(dataframe["Pclass"] == 3) & (dataframe["Age"] < 35) ]
#dataframe2 = dataframe[dataframe["Age"] <= 35 ]

             #and dataframe[dataframe["Age"] <35]
#dataframe2 = dataframe[dataframe["Age"] <35]

# preguntamos si es verdadero o falso e iteramos
for i in dataframe["Survived"]:
    total = total + 1
    if i == True:
        contador = contador + 1

porcentaje = (contador / total)*100

print(total)
print(contador)
print(round(porcentaje , 2))




"""
dataframe2 = pd.unique(dataframe["Pclass"])

dataframe2["Pclass"] = pd.Series([dataframe["Pclass"] >= 3])

dataframe2["Age"] = pd.Series([dataframe["Age"] > 35])

#x para Pclass
x = dataframe.index[:,2]
#y para las edades
y = dataframe.index[:,5]

dataframe2 = dataframe["Pclass"] == 3
dataframe2 = dataframe["Age"] >35

print(np.where(dataframe["Pclass"] == 3 ))
print(dataframe2)
"""



