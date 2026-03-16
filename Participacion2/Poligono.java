package Participacion2;

public class Poligono {

    //Un campo de datos privado int llamado n que define el número de lados del polígono con un valor predeterminado de 3.
    //Un campo de datos privado double llamado lado que almacena la longitud del lado con un valor predeterminado de 1.
    //Un campo de datos privado double llamado x que define la coordenada x del centro del polígono con un valor predeterminado de 0. 
    //Un campo de datos privado double llamado y que define la coordenada y del centro del polígono con un valor predeterminado de 0.
    private int n;
    private double lado;
    private double x;
    private double y;

    //Un constructor sin argumentos que crea un polígono regular con valores predeterminados.
    public Poligono() {
        this.n = 3;
        this.lado = 1;
        this.x = 0;
        this.y = 0;
    }

    //Un constructor que crea un polígono regular con el número de lados y la longitud especificados, centrado en (0, 0).
    public Poligono(int n, double lado) {
        this.n = n;
        this.lado = lado;
        this.x = 0;
        this.y = 0;
    }

    //Un constructor que crea un polígono regular con el número de lados, la longitud del lado y las coordenadas x e y especificados.
    public Poligono(int n, double lado, double x, double y) {
        this.n = n;
        this.lado = lado;
        this.x = x;
        this.y = y;
    }

    //El método getPerimetro() retorna el perímetro del polígono.
    public double getPerimetro() {
        return this.n * this.lado;
    }

    //El método getArea() retorna el área del polígono. 
    public double getArea(){
        return (n * Math.pow(lado,2)) / (4 * Math.tan(Math.PI / n));
    }

    @Override
    public String toString() {
        return "Poligono(lados=" + this.n + ", lado=" + this.lado + ", centro=(" + this.x + "," + this.y + "))";
    }
}
