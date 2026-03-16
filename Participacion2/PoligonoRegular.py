import math

class PoligonoRegular:

    # Un constructor sin argumentos que crea un polígono regular con valores predeterminados.
    # Un constructor que crea un polígono regular con el número de lados y la longitud especificados, centrado en (0, 0).
    # Un constructor que crea un polígono regular con el número de lados, la longitud del lado y las coordenadas x e y especificados.
    # (En Python todo esto se logra con un solo constructor usando parámetros por defecto)
    def __init__(self, n=3, lado=1.0, x=0.0, y=0.0):
        # Un campo de datos privado int llamado n que define el número de lados del polígono con un valor predeterminado de 3.
        self.__n = n
        
        # Un campo de datos privado double llamado lado que almacena la longitud del lado con un valor predeterminado de 1.
        self.__lado = lado
        
        # Un campo de datos privado double llamado x que define la coordenada x del centro del polígono con un valor predeterminado de 0. 
        self.__x = x
        
        # Un campo de datos privado double llamado y que define la coordenada y del centro del polígono con un valor predeterminado de 0.
        self.__y = y

    # El método getPerimetro() retorna el perímetro del polígono.
    def getPerimetro(self):
        return self.__n * self.__lado

    # El método getArea() retorna el área del polígono. 
    def getArea(self):
        return (self.__n * math.pow(self.__lado, 2)) / (4 * math.tan(math.pi / self.__n))

    def __str__(self):
        return "Poligono(lados=" + str(self.__n) + ", lado=" + str(self.__lado) + ", centro=(" + str(self.__x) + "," + str(self.__y) + "))"


class Main:
    def __init__(self):
        # Constructor sin argumentos
        p1 = PoligonoRegular()
        print("Poligono 1")
        print(p1)
        print("Perímetro: {:.2f}".format(p1.getPerimetro()))
        print("Área: {:.5f}\n".format(p1.getArea()))

        # Constructor(6, 4)
        p2 = PoligonoRegular(6, 4)
        print("Poligono 2")
        print(p2)
        print("Perímetro: {:.2f}".format(p2.getPerimetro()))
        print("Área: {:.5f}\n".format(p2.getArea()))

        # Constructor(10, 4, 5.6, 7.8)
        p3 = PoligonoRegular(10, 4, 5.6, 7.8)
        print("Poligono 3")
        print(p3)
        print("Perímetro: {:.2f}".format(p3.getPerimetro()))
        print("Área: {:.5f}".format(p3.getArea()))

# Ejecución del programa
Main()