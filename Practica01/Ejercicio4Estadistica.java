/**
* Clase Estadistica.
*
* @author Ever Conde
* @version 1.0 04/03/2026
*/


import java.util.Scanner;

// ORIENTADA A OBJETOS 
class Estadistica {

    private double[] datos;

    public Estadistica(double[] datos) {
        this.datos = datos;
    }

    public double promedio() {
        double suma = 0;
        for (double x : datos) {
            suma += x;
        }
        return suma / datos.length;
    }

    public double desviacion() {
        double prom = this.promedio();
        double sumaCuadrados = 0;
        for (double x : datos) {
            sumaCuadrados += Math.pow(x - prom, 2);
        }

        return Math.sqrt(sumaCuadrados / (datos.length - 1));
    }
}
// MODULAR ESTRUCTURADA
public class Ejercicio4Estadistica {
    
    public static double calcularPromedio(double[] vect) {
        double suma = 0;
        for (double x : vect) {
            suma += x;
        }
        return suma / vect.length;
    }

    public static double calcularDesviacion(double[] vect) {
        double prom = calcularPromedio(vect);
        double sumaCuadrados = 0;
        for (double x : vect) {
            sumaCuadrados += Math.pow(x - prom, 2);
        }
        return Math.sqrt(sumaCuadrados / (vect.length - 1));
    }

    public static void main(String[] args) {

        double[] arr = {1.9, 2.5, 3.7, 2, 1, 6, 3, 4, 5, 2};

        Estadistica est = new Estadistica(arr);

        System.out.printf("El promedio es %.2f\n", est.promedio());
        System.out.printf("La desviacion standard es %.5f\n", est.desviacion());
    }
}