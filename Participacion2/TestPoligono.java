package Participacion2;

class TestPoligono {
    public static void main(String[] args) {
        
        //Constructor sin argumentos
        Poligono p1 = new Poligono();
        System.out.println("Poligono 1");
        System.out.println(p1.toString());
        System.out.printf("Perimetro: %.2f\n", p1.getPerimetro());
        System.out.printf("Area: %.5f\n\n", p1.getArea());

        //Constructor(6, 4)
        Poligono p2 = new Poligono(6, 4);
        System.out.println("Poligono 2");
        System.out.println(p2.toString());
        System.out.printf("Perimetro: %.2f\n", p2.getPerimetro());
        System.out.printf("Area: %.5f\n\n", p2.getArea());

        //Constructor(10, 4, 5.6, 7.8) 
        Poligono p3 = new Poligono(10, 4, 5.6, 7.8);
        System.out.println("Poligono 3");
        System.out.println(p3.toString());
        System.out.printf("Perimetro: %.2f\n", p3.getPerimetro());
        System.out.printf("Area: %.5f\n", p3.getArea());
    }
}