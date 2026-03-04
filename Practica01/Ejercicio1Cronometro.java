/**
* Clase Ejercicio1Cronometro.
*
* @author Ever Conde
* @version 1.0 04/03/2026
*/

public class Ejercicio1Cronometro {

    private int inicia;
    private int finaliza;

    public Ejercicio1Cronometro() {
        this.inicia = (int) System.currentTimeMillis();
    }

    public int getInicia() {
        return inicia;
    }

    public int getFinaliza() {
        return finaliza;
    }

    public void inicia() {
        this.inicia = (int) System.currentTimeMillis();
    }

    public void detener() {
        this.finaliza = (int) System.currentTimeMillis();
    }

    public int lapsoDeTiempo() {
        return finaliza - inicia;
    }
}
