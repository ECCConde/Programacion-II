import time
import random

class Cronometro:
    def __init__(self):
        self._inicia = 0
        self._finaliza = 0

    def inicia(self):
        self._inicia = int(time.time() * 1000)

    def detener(self):
        self._finaliza = int(time.time() * 1000)

    def lapsoDeTiempo(self):
        return self._finaliza - self._inicia

class Main:
    def main(self):
  
        cr = Cronometro()
  
        cantidad = 10000 
        min_val = 1
        max_val = 10000
        lista = []     

        for i in range(cantidad):
            lista.append(random.randint(min_val, max_val))

        print(f"Numeros Desordenados ({cantidad})")
        for num in lista:
            print(f"{num} ", end="")
        print("\n")


        print("espere")
        cr.inicia()

        n = len(lista)
        for i in range(n - 1):

            min_idx = i
            for j in range(i + 1, n):
                if lista[j] < lista[min_idx]:
                    min_idx = j
            

            temp = lista[min_idx]
            lista[min_idx] = lista[i]
            lista[i] = temp

        cr.detener()
    
        print(f"\n Numeros Ordenados ({cantidad}) ")
        for num in lista:
            print(f"{num} ", end="")
        print("\n")

        print(f"Lapso de tiempo: {cr.lapsoDeTiempo()} ms")

if __name__ == "__main__":
    ejecutar = Main()
    ejecutar.main()