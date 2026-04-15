from adivinanumero import AdivinaNumero
from adivinapar import AdivinaPar
from adivinaimpar import AdivinaImpar

class Aplicacion:
    def main(self):
        # a) Crea una instancia de cada uno de los tres juegos... número de vidas 3.
        j1 =AdivinaNumero(3)
        j2 =AdivinaPar(3)
        j3 =AdivinaImpar(3)

        # b) Llame al metodo juega de cada una de las tres instancias.
        print("Juego 1: Normal")
        j1.juega()

        print("\nJuego 2: Par")
        j2.juega()

        print("\nJuego 3: Impar")
        j3.juega()

if __name__ == "__main__":
    Aplicacion().main()