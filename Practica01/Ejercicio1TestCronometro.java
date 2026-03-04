import java.util.Random;

public class Ejercicio1TestCronometro {

    public static void main(String[] args) {

        Ejercicio1Cronometro cr = new Ejercicio1Cronometro();
        Random rand = new Random();
        
        int cantidad = 1000;  
        int min = 1;
        int max = 1000;
        int[] lista = new int[cantidad];

        for (int i = 0; i < cantidad; i++) {
            lista[i] = rand.nextInt((max - min) + 1) + min;
        }

        System.out.println(" Numeros Ramdon (" + cantidad + ") ");
        for (int i = 0; i < cantidad; i++) {
            System.out.print(lista[i] + " ");
        }
        System.out.println("\n");

        System.out.println("Espere");
        cr.inicia(); 

        int n = lista.length;
        for (int i = 0; i < n - 1; i++) {

            int minIdx = i;
            for (int j = i + 1; j < n; j++) {
                if (lista[j] < lista[minIdx]) {
                    minIdx = j;
                }
            }
            
            int temp = lista[minIdx];
            lista[minIdx] = lista[i];
            lista[i] = temp;
        }
        
        cr.detener(); 

        System.out.println("\n Numeros Ordenados (" + cantidad + ")");
        for (int i = 0; i < cantidad; i++) {
            System.out.print(lista[i] + " ");
        }
        System.out.println("\n");

        System.out.println("Lapso de tiempo: " + cr.lapsoDeTiempo() + " ms");
    }
}