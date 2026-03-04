public class Ejercicio2EcuacionLineal {
    private double a, b, c, d, e, f;

    public Ejercicio2EcuacionLineal(double a, double b, double c, double d, double e, double f) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.d = d;
        this.e = e;
        this.f = f;
    }

    public boolean tieneSolucion() {

        double x = this.a * this.d - this.b * this.c;

        if (x != 0.0) {
            return true;
        } else {
            return false;
        }
    }

    public String getX() {
        if (this.tieneSolucion()) {
            double x = this.a * this.d - this.b * this.c;
            double resultado = (this.e * this.d - this.b * this.f) / x;
            return String.valueOf(resultado);
        } else {
            return "No tiene solución";
        }
    }

    public String getY() {
        if (this.tieneSolucion()) {
            double x = this.a * this.d - this.b * this.c;
            double resultado = (this.a * this.f - this.e * this.c) / x;
            return String.valueOf(resultado);
        } else {
            return "No tiene solución";
        }
    }

    @Override
    public String toString() {
        return a + "," + b + "," + c + "," + d + "," + e + "," + f;
    }

    public static void main(String[] args) {
        
        Ejercicio2EcuacionLineal t1 = new Ejercicio2EcuacionLineal(9.0, 4.0, 3.0, -5.0, -6.0, -21.0);
        System.out.println("¿Tiene solución?: " + t1.tieneSolucion());
        System.out.println("Solución de X: " + t1.getX());
        System.out.println("Solución de Y: " + t1.getY());

        System.out.println(); 
        Ejercicio2EcuacionLineal t2 = new Ejercicio2EcuacionLineal(1.0, 2.0, 2.0, 4.0, 4.0, 5.0);
        System.out.println("¿Tiene solución?: " + t2.tieneSolucion());
        System.out.println("Solución de X: " + t2.getX());
        System.out.println("Solución de Y: " + t2.getY());
    }
}