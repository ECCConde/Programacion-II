import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getDiscriminante(self):
        return math.pow(self.b, 2) - (4 * self.a * self.c)

    def getRaiz1(self):
        disc = self.getDiscriminante()
        if disc < 0: return 0
        return (-self.b + math.sqrt(disc)) / (2 * self.a)

    def getRaiz2(self):
        disc = self.getDiscriminante()
        if disc < 0: return 0
        return (-self.b - math.sqrt(disc)) / (2 * self.a)

class Main:
    def __init__(self):
        while True:
            print("Ingrese a, b, c: ", end="")
            entrada = input().split()
            
            a = float(entrada[0])
            b = float(entrada[1])
            c = float(entrada[2])

            eq = EcuacionCuadratica(a, b, c)
            disc = eq.getDiscriminante()

            if disc > 0:
                print("La ecuacion tiene dos raices: {:.6f} y {:.6f}".format(eq.getRaiz1(), eq.getRaiz2()))
            elif disc == 0:
                print("La ecuación tiene una raiz: " + str(eq.getRaiz1()))
            else:
                print("La ecuacion no tiene raices reales")

Main()