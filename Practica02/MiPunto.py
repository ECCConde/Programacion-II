import math
from multimethod import multimethod

class MiPunto:
    #  Los atributos x e y que representan las coordenadas con m´etodos getter
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    # b) Un constructor sin argumentos que crea un punto (0, 0).
    # c) Un constructor que construye un punto con las coordenadas especificadas.
    def __init__(self, x=0.0, y=0.0):
        self.__x = x  
        self.__y = y

    
    # d) Un metodo llamado distancia que retorna la distancia desde este punto hasta un punto especificado del tipo MiPunto.
    @multimethod
    def distancia(self, p: "MiPunto"):
        
        dist = math.sqrt((p.getX() - self.__x)**2 + (p.getY() - self.__y)**2)
        return dist

    # e) Un metodo llamado distancia que retorna la distancia desde este punto hasta otro punto con las coordenadas x e y especificadas.
    @multimethod
    def distancia(self, x: float, y: float):
        dist = math.sqrt((x - self.__x)**2 + (y - self.__y)**2)
        return dist

    # (MAIN)
class MainPunto:
    def main(self):
        p1 = MiPunto()
        p2 = MiPunto(10.0, 30.5)
        
        print(f"Distancia entre p1 y p2: {p1.distancia(p2):.4f}")
        
        print(f"Distancia a coordenadas(10, 30.5): {p1.distancia(10.0, 30.5):.4f}")

ejecutar = MainPunto()
ejecutar.main()