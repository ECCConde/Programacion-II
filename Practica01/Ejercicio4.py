import math
# ORIENTADA A OBJETOS 
class Estadistica:
    def __init__(self, datos):
        self.datos = datos

    def promedio(self):
        return sum(self.datos) / len(self.datos)

    def desviacion(self):
        prom = self.promedio()
        suma_cuadrados = sum((x - prom) ** 2 for x in self.datos)
        return math.sqrt(suma_cuadrados / (len(self.datos) - 1))

#MODULAR ESTRUCTURADA
def promedio(vect):
    return sum(vect) / len(vect)

def desviacion(vect):
    prom = promedio(vect)
    suma_cuadrados = sum((x - prom) ** 2 for x in vect)
    return math.sqrt(suma_cuadrados / (len(vect) - 1))


##########################################
arr = [1.9, 2.5, 3.7, 2, 1, 6, 3, 4, 5, 2]

class Main():
    def __init__(self):
        est = Estadistica(arr)
        
        print("El promedio es {:.2f}".format(est.promedio()))
        print("La desviacion standard es {:.5f}".format(est.desviacion()))

Main()