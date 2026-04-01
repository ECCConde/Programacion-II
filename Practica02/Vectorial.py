import math
from multimethod import multimethod

class Vectorial:
    
    def __init__(self, a1=0.0, a2=0.0, a3=0.0):
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3


    def __modulo(self):
        return math.sqrt((self.__a1 ** 2) + (self.__a2 ** 2) + (self.__a3 ** 2))
        
    def mostrar(self):
        print(f"({self.__a1}, {self.__a2}, {self.__a3})")
    
    # a) Perpendicular. Si el vector a es ortogonal o perpendicular a b: |a + b| = |a − b|
    @multimethod
    def perpendicular(self, b: "Vectorial", opcion: int):
        sum_a1 = self.__a1 + b.__a1
        sum_a2 = self.__a2 + b.__a2
        sum_a3 = self.__a3 + b.__a3
        mod_suma = math.sqrt((sum_a1**2) + (sum_a2**2) + (sum_a3**2))
        
        
        res_a1 = self.__a1 - b.__a1
        res_a2 = self.__a2 - b.__a2
        res_a3 = self.__a3 - b.__a3
        mod_resta = math.sqrt((res_a1**2) + (res_a2**2) + (res_a3**2))
        
        return mod_suma == mod_resta

    # b) Perpendicular. Si el vector a es mutuamente ortogonal a b: |a − b| = |b − a|
    @multimethod
    def perpendicular(self, b: "Vectorial", opcion: float):

        res1_a1 = self.__a1 - b.__a1
        res1_a2 = self.__a2 - b.__a2
        res1_a3 = self.__a3 - b.__a3
        mod_res1 = math.sqrt((res1_a1**2) + (res1_a2**2) + (res1_a3**2))

        res2_a1 = b.__a1 - self.__a1
        res2_a2 = b.__a2 - self.__a2
        res2_a3 = b.__a3 - self.__a3
        mod_res2 = math.sqrt((res2_a1**2) + (res2_a2**2) + (res2_a3**2))
        
        return mod_res1 == mod_res2

    # c) Perpendicular. Si el vector a es ortogonal a b: a · b = 0
    @multimethod
    def perpendicular(self, b: "Vectorial", opcion: str):
        productopunto = (self.__a1 * b.__a1) + (self.__a2 * b.__a2) + (self.__a3 * b.__a3)
        return productopunto == 0.0

    # d)  Perpendicular. Si el vector a es ortogonal a b: |a + b|^2 = |a|^2 + |b|^2
    @multimethod
    def perpendicular(self, b: "Vectorial", opcion: bool):
        sum_a1 = self.__a1 + b.__a1
        sum_a2 = self.__a2 + b.__a2
        sum_a3 = self.__a3 + b.__a3
        mod_suma_cuadrado = (sum_a1**2) + (sum_a2**2) + (sum_a3**2)
        
        acuadrado = (self.__a1**2) + (self.__a2**2) + (self.__a3**2)
        bcuadrado = (b.__a1**2) + (b.__a2**2) + (b.__a3**2)
        
        return mod_suma_cuadrado == (acuadrado + bcuadrado)

    # e) Paralela. Si el vector a es paralela a b: a = rb
    @multimethod
    def paralela(self, b: "Vectorial", opcion: int):
        condicion1 = (self.__a1 * b.__a2) == (self.__a2 * b.__a1)
        condicion2 = (self.__a2 * b.__a3) == (self.__a3 * b.__a2)
        condicion3 = (self.__a1 * b.__a3) == (self.__a3 * b.__a1)
        return condicion1 and condicion2 and condicion3

    # f ) Paralela. Si el vector a es paralela a b: a × b = 0
    @multimethod
    def paralela(self, b: "Vectorial", opcion: float):
        c1 = (self.__a2 * b.__a3) - (self.__a3 * b.__a2)
        c2 = (self.__a3 * b.__a1) - (self.__a1 * b.__a3)
        c3 = (self.__a1 * b.__a2) - (self.__a2 * b.__a1)
        
        return c1 == 0.0 and c2 == 0.0 and c3 == 0.0

   
    # g)  Proyeccion de a sobre b. La proyeccion ortogonal de a sobre b:Proy_b a = ((a . b) / |b|^2) * b
    def proyeccion_de_a_sobre_b(self, b: "Vectorial"):
        productopunto = (self.__a1 * b.__a1) + (self.__a2 * b.__a2) + (self.__a3 * b.__a3)
        bcuadrado = (b.__a1**2) + (b.__a2**2) + (b.__a3**2)
        
        factorescal = productopunto / bcuadrado
        
        return Vectorial(factorescal * b.__a1, factorescal * b.__a2, factorescal * b.__a3)

    
    # h)  Componente de a en b. El componente de a en la direccion de b: Comp_b a = (a . b) / |b|
    def componente_de_a_en_b(self, b: "Vectorial"):
        productopunto = (self.__a1 * b.__a1) + (self.__a2 * b.__a2) + (self.__a3 * b.__a3)
        modulo_b = b.__modulo() 
        
        return productopunto / modulo_b


# (MAIN)

class Main:
    def main(self):
    
        vector_x = Vectorial(1.0, 0.0, 0.0)
        vector_y = Vectorial(0.0, 1.0, 0.0)
     
        v1 = Vectorial(2.0, 4.0, 6.0)
        v2 = Vectorial(1.0, 2.0, 3.0)
        
        print("1.Determinar si dos vectores son perpendiculares")
        print("Por formula a (|a+b|=|a-b|):", vector_x.perpendicular(vector_y, 1))
        print("Por formula b (|a-b|=|b-a|):", vector_x.perpendicular(vector_y, 1.0))
        
        print("\n2.Determinar si dos vectores son paralelos, ")
        print("Por formula e (a = r*b):", v1.paralela(v2, 1))
        print("Por formula f (a x b = 0):", v1.paralela(v2, 1.0))

        print("\n3y4.Determinar la proyeccion de dos vectores y  determinar el componente de dos vectores ")
        proy = v1.proyeccion_de_a_sobre_b(v2)
        print("Proyección de v1 sobre v2: ", end="")
        proy.mostrar()
        
        comp = v1.componente_de_a_en_b(v2)
        print(f"Componente de v1 en v2: {comp}")

ejecutar = Main()
ejecutar.main()