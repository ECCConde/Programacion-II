import math

class Vector3D:
    def __init__(self, a1=0.0, a2=0.0, a3=0.0):
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3

    def mostrar(self):
        print(f"({self.__a1:.2f}, {self.__a2:.2f}, {self.__a3:.2f})")

    # a) Suma de dos vectores a y b: c = a + b = (a1 + b1, a2 + b2, a3 + b3)
    def __add__(self, b: "Vector3D"):
        res_a1 = self.__a1 + b.__a1
        res_a2 = self.__a2 + b.__a2
        res_a3 = self.__a3 + b.__a3
        return Vector3D(res_a1, res_a2, res_a3)

    # c) Longitud de un vector a: |a| = sqrt(a1^2 + a2^2 + a3^2)
    def __abs__(self):
        suma_cuadrados = (self.__a1**2) + (self.__a2**2) + (self.__a3**2)
        return math.sqrt(suma_cuadrados)

    # d) Normal de un vector a: b = a / |a| = (a1/|a|, a2/|a|, a3/|a|)
    def __pos__(self):
        longitud = abs(self) 
        if longitud == 0:
            return Vector3D(0, 0, 0) 
            
        n_a1 = self.__a1 / longitud
        n_a2 = self.__a2 / longitud
        n_a3 = self.__a3 / longitud
        return Vector3D(n_a1, n_a2, n_a3)

    # Sobrecarga del Operador (*) para los incisos b, e, y f
    def __mul__(self, otro):
        
        # b) Multiplicacion de un escalar r por un vector a: b = ra = (r*a1, r*a2, r*a3)
        if isinstance(otro, int) or isinstance(otro, float):
            return Vector3D(self.__a1 * otro, self.__a2 * otro, self.__a3 * otro)
            
        # e) Producto escalar de a y b: a · b = a1b1 + a2b2 + a3b3
        elif isinstance(otro, Vector3D):
            return (self.__a1 * otro.__a1) + (self.__a2 * otro.__a2) + (self.__a3 * otro.__a3)
            
        # f) Producto vectorial de a y b: a x b = (a2b3 - a3b2, a3b1 - a1b3, a1b2 - a2b1)
        else:
            print("Operación no válida.")
            return None
            
    def __pow__(self, b: "Vector3D"):
        c1 = (self.__a2 * b.__a3) - (self.__a3 * b.__a2)
        c2 = (self.__a3 * b.__a1) - (self.__a1 * b.__a3)
        c3 = (self.__a1 * b.__a2) - (self.__a2 * b.__a1)
        return Vector3D(c1, c2, c3)


#(MAIN)
class Main:
    def main(self):
        v1 = Vector3D(1.0, 2.0, 3.0)
        v2 = Vector3D(4.0, 5.0, 6.0)
        
        print("Vector a: ", end="")
        v1.mostrar()
        print("Vector b: ", end="")
        v2.mostrar()
        print("-" * 30)
        
        print("a) Suma de dos vectores: ", end="")
        v_suma = v1 + v2
        v_suma.mostrar()

        print("b) Multiplicación por escalar : ", end="")
        v_escalar = v1 * 3.0
        v_escalar.mostrar()

        print(f"c) Longitud del vector: {abs(v1):.4f}")

        print("d) Normal de un vector: ", end="")
        v_normal = +v1
        v_normal.mostrar()

        print("e) Producto escalar: ", end="")
        prod_escalar = v1 * v2
        print(prod_escalar)

        print("f) Producto vectorial: ", end="")
        prod_vectorial = v1 ** v2
        prod_vectorial.mostrar()

ejecutar3 = Main()
ejecutar3.main()