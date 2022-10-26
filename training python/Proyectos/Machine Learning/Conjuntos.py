#Conjuntos

#conjunto = {1,2,3,4,5,"Aldo",("Angelica","Sonia")}
#print(conjunto)

set = {1,2,3,4,5.6}
set.add(5)
print(set)
#set.clear()
#print(set)
set.discard(2)
print(set)

A = {1,2,3,4,5}
B = {4,5,6,7,8}

#union
print(A | B) #alt 124
#interseccion
print(A & B)
#diferencia
print(A - B)
#diferencia simetrica
print(A ^ B)

