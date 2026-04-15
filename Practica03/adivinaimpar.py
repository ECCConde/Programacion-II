from adivinanumero import AdivinaNumero
    # a) Se deriva de la clase JuegoAdivinaNumero
class AdivinaImpar(AdivinaNumero):

    # b) Redefina el metodo validaNumero devolviendo true si el número es impar y si está entre el 0 y 10.
    def validaNumero(self, n: int) -> bool:
        if super().validaNumero(n) and n % 2 != 0:
            return True
        if n % 2 == 0:
            print("Error: debe ser impar")
        return False