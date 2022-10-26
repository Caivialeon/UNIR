
class Numero:
    entero = 0
    def __init__(self , e):
        self.entero = e
        self.normal = self.entero
        self.romano = self.convertir_a_romano(e)

    def convertir_a_romano(self,enteros):
        numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerales = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        numeral = ""

        i = 0
        while enteros > 0:
            for _ in range(enteros // numeros[i]):
                numeral += numerales[i]
                enteros -= numeros[i]
            i += 1
        return str(numeral)

    def imprime(self):
        print(f"{self.normal}" + " " + self.romano)

    def suma_romano(self,roma):
        self.normal += self.convertir_a_entero(str(roma))
        self.romano = str(self.convertir_a_romano(self.normal))

    def convertir_a_entero(self, s):
        a = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        for i in range(len(str(s))):
            if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
                ans -= a[s[i]]
            else:
                ans += a[s[i]]
        return ans

    def is_romano(self, r):
            numerales = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
            for i in range(len(r)):
                if r[i] in numerales:
                    l = True
                else:
                    l = False
                    print("no es numero romano")
                    break

            return l



class MejorNumero(Numero):

    def __init__(self, a):
        Numero.__init__(self, a)
        self.normal = a
        self.romano = Numero.convertir_a_romano(self,self.normal)

    def imprimes(self):
        print(f"{self.normal}" + " " + self.romano)


    def resta(self,r):
        self.normal -= Numero.convertir_a_entero(self, str(r))
        self.romano = Numero.convertir_a_romano(self , self.normal)

    def multiplica(self,r):
        self.normal *= Numero.convertir_a_entero(self, str(r))
        self.romano = Numero.convertir_a_romano(self , self.normal)

    def iterar(self,lista):
        suma = 0
        for i in range(len(lista)):
            try:
                Numero.suma_romano(self,lista[i])
            except:
                print(f"Ha fallado el numero {lista[i]}")








mn = MejorNumero(160)
#mn.imprimes()
#mn.resta("X")
#mn.imprimes()
#mn.multiplica("X")
mn.iterar(["XX", 675 , "VI"])
mn.imprimes()

"""
n = Numero(1672)

n.imprime()
n.suma_romano("XXX")
n.imprime()
"""
"""
n = Numero(1672)
print(n.is_romano("Hola"))"""