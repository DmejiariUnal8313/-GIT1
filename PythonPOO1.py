def mcd (m,n):
    while m%n != 0:
        mViejo = m
        nViejo = n
        m = nViejo
        n = mViejo%nViejo
    return n

#definicion de la clase
class Fraccion:
        def __init__(self,arriba,abajo):
            self.num = arriba
            self.den = abajo
        def mostrar (self):
            print (self.num,'/',self.den)
        def __str__(self):
            return str(self.num)+"/"+str(self.den)
        def __add__(self,otraFraccion):
            nuevoNum = self.num*otraFraccion.den + \
            self.den*otraFraccion.num
            nuevoDen = self.den*otraFraccion.den
            comun = mcd(nuevoNum,nuevoDen)
            return Fraccion(nuevoNum//comun,nuevoDen//comun)
        def __sub__(self,otraFraccion):
            nuevoNum = self.num*otraFraccion.den - \
            self.den*otraFraccion.num
            nuevoDen = self.den*otraFraccion.den
            comun = mcd(nuevoNum,nuevoDen)
            return Fraccion(nuevoNum//comun,nuevoDen//comun)
        def __mul__(self,otraFraccion):
            nuevoNum = self.num*otraFraccion.den * \
            self.den*otraFraccion.num
            nuevoDen = self.den*otraFraccion.den
            comun = mcd(nuevoNum,nuevoDen)
            return Fraccion(nuevoNum//comun,nuevoDen//comun)
        def __truediv__(self,otraFraccion):
            nuevoNum = self.num*otraFraccion.den
            nuevoDen = self.den*otraFraccion.num
            comun = mcd(nuevoNum,nuevoNum)
            return Fraccion (nuevoNum//comun,nuevoDen//comun)
#Programa Principal
miFraccion = Fraccion(3, 5)
print (miFraccion)
print ("Comí", miFraccion, "de la pizza")
miFraccion.__str__()
str(miFraccion)
print(type(miFraccion))
f1 = Fraccion(1, 4)
f2 = Fraccion(1, 2)
f3 = f1+f2
f4 = f1-f2
f5 = f1*f2
f6 = f1/f2
print(f3)
print(f4)
print(f5)
print(f6)



