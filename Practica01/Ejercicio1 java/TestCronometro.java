package ejercicio1;

import java.util.Random;

public class TestCronometro {

    public static void main(String[] args) {

        Cronometro cr = new Cronometro();
        Random rand = new Random();
        
        int cantidad = 1000;  
        int min = 1;
        int max = 1000;
        int[] arr = new int[cantidad];

        for (int i = 0; i < cantidad; i++) {
            arr[i] = rand.nextInt((max - min) + 1) + min;
        }

        System.out.println(" Numeros Ramdon (" + cantidad + ") ");
        for (int i = 0; i < cantidad; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println("\n");

        System.out.println("Espere");
        cr.inicia(); 

        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {

            int minIdx = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }
            
            int temp = arr[minIdx];
            arr[minIdx] = arr[i];
            arr[i] = temp;
        }
        
        cr.detener(); 

        System.out.println("\n Numeros Ordenados (" + cantidad + ")");
        for (int i = 0; i < cantidad; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println("\n");

        System.out.println("Lapso de tiempo: " + cr.lapsoDeTiempo() + " ms");
    }
}