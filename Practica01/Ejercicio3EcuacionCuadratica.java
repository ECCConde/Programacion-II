import java.util.Scanner;

public class Ejercicio3EcuacionCuadratica {
    private double a;
    private double b;
    private double c;

    public Ejercicio3EcuacionCuadratica(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public double getDiscriminante() {
        return Math.pow(this.b, 2) - (4 * this.a * this.c);
    }

    public double getRaiz1() {
        double disc = getDiscriminante();
        if (disc < 0) return 0;
        return (-this.b + Math.sqrt(disc)) / (2 * this.a);
    }

    public double getRaiz2() {
        double disc = getDiscriminante();
        if (disc < 0) return 0;
        return (-this.b - Math.sqrt(disc)) / (2 * this.a);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        while (true) {
            System.out.print("Ingrese a, b, c: ");
            
            double a = input.nextDouble();
            double b = input.nextDouble();
            double c = input.nextDouble();

            Ejercicio3EcuacionCuadratica eq = new Ejercicio3EcuacionCuadratica(a, b, c);
            double disc = eq.getDiscriminante();

            if (disc > 0) {
                System.out.printf("La ecuacion tiene dos raices: %.6f y %.6f\n", 
                    eq.getRaiz1(), eq.getRaiz2());
            } else if (disc == 0) {
                System.out.println("La ecuación tiene una raiz: " + eq.getRaiz1());
            } else {
                System.out.println("La ecuacion no tiene raices reales");
            }
           
        }
    }
}