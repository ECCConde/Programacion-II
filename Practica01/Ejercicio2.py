class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def tieneSolucion(self):

        x = self.a * self.d - self.b * self.c 
        
        if x != 0.0:
            return True
        else:
            return False

    def getX(self):
        if self.tieneSolucion():
           
            x = self.a * self.d - self.b * self.c
            return (self.e * self.d - self.b * self.f) / x
        else:
            return "No tiene solución"

    def getY(self):
        if self.tieneSolucion():
            x = self.a * self.d - self.b * self.c
            return (self.a * self.f - self.e * self.c) / x
        else:
            return "No tiene solución"

    def __str__(self):
        return "{},{},{},{},{},{}".format(self.a, self.b, self.c, self.d, self.e, self.f)


t1 = EcuacionLineal(9.0, 4.0, 3.0, -5.0, -6.0, -21.0)
print("¿Tiene solución?:", t1.tieneSolucion())
print("Solución de X:", t1.getX())
print("Solución de Y:", t1.getY())

print("\n")
t2 = EcuacionLineal(1.0, 2.0, 2.0, 4.0, 4.0, 5.0)
print("¿Tiene solución?:", t2.tieneSolucion()) 
print("Solución de X:", t2.getX())
print("Solución de Y:", t2.getY())