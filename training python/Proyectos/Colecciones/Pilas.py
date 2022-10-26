#pilas no existen, se usan listas para simularlo.

pila = [1,2,3]
print(pila)
#agregando elementos por el final
pila.append(4)
pila.append(5)
print (pila)
#Sacando elementos por el final
n = pila.pop()
print(f"sacando el elemento {n}")
print(pila)