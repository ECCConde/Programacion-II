class Juego:
    def __init__(self, v: int):
    # a) Añada los atributos numeroDeVidas y record ambos de tipo entero.
        self.__vi = v
        self.__v = v
        self.__rec = 0

    # b) Añada el metodo reiniciaPartida.
    def reiniciaPartida(self):
        self.__v = self.__vi

    # c) Añada el metodo actualizaRecord.
    def actualizaRecord(self):
        self.__rec += 1
        print(f"Record: {self.__rec}")

    # d) Añada el metodo quitaVida.
    def quitaVida(self) -> bool:
        self.__v -= 1
        return self.__v > 0