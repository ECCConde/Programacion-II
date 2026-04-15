# Importamos la clase hija
from adivinanumero import AdivinaNumero
class Aplicacion1:
    def main(self):
        # Crea instancia de JuegoAdivinaNumero con 3 vidas y llama al metodo juega
        j1 = AdivinaNumero(3)
        j1.juega()

if __name__ == "__main__":
    app = Aplicacion1()
    app.main()