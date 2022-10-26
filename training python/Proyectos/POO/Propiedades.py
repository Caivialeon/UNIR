#propiedades()

class Empleado:
    def __init__(self,nombre,salario):
        self.__nombre = nombre
        self.__salario = salario
    def __getnombre(self):
        return self.__nombre
    def __getsalario(self):
        return self.__salario
    def __setnombre(self,nombre):
        self.__nombre = nombre
    def __setsalario(self,salario):
        self.__salario = salario
    def __delnombre(self):
        del self.__nombre
    def __delsalario(self):
        del self.__salario

    nombre = property(fget = __getnombre,fset = __setnombre , fdel = __delnombre)
    salario = property(fget = __getsalario,fset = __setsalario , fdel = __delsalario)

emp1= Empleado("Aldo" , 25000)
emp1.nombre = "Aldo Alberto"
print(emp1.nombre , emp1.salario)
'''
emp1= Empleado("Aldo" , 25000)
print(emp1.getnombre())
print(emp1.getsalario())
emp1.setnombre("Aldo Alberto")
print(emp1.getnombre())
'''