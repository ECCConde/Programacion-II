import random
from juego import Juego
# a) Se deriva de la clase Juego.
class AdivinaNumero(Juego):
    # b) Añada el atributo numeroAAdivinar de tipo entero.
    # c) Agregue un constructor que tiene el parámetro número de vidas
    #    Este se lo pasará al constructor de la clase padre.
    def __init__(self, v: int):
        super().__init__(v)
        self.__num = 0

    # Juego 2 a) Añada un nuevo metodo validaNumero (entre 0 y 10).
    def validaNumero(self, n: int) -> bool:
        return 0 <= n <= 10

    # d) Agregue el metodo juega, que tendrá la siguiente implementación:
    def juega(self):
    # 1) Llama al metodo reiniciaPartida que ha heredado.
        self.reiniciaPartida()

        while True:
    # 2) Genere aleatoriamente el número a adivinar (entre 0 y 10).
            self.__num = random.randint(0, 10)
            if self.validaNumero(self.__num):
                break

        while True:
            try:
    # 3) Muestra un mensaje al usuario pidiendo que adivine.
                intento = int(input("Adivina numero (0-10): "))
            except ValueError:
                continue

    # Juego 2 b) Utilice el metodo validaNumero para validar el número ingresado.
            if not self.validaNumero(intento):
                print("Invalido")
                continue

    # 4) Lee un entero del teclado y lo compara...
            if intento == self.__num:
                # a. Si es igual, muestra Acertaste y llama a actualizaRecord.
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
    # b. Si es diferente, llama al metodo quitaVida heredado.
                if self.quitaVida():
    # c. Si devuelve true (quedan vidas), indica mayor o menor.
                    if self.__num > intento:
                        print("Mayor")
                    else:
                        print("Menor")
                else:
    # d. Si devuelve false (sin vidas), sale del metodo juega.
                    print(f"Sin vidas. Era {self.__num}")
                    break