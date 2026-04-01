/**
* Clase Ejercicio1Cronometro.
*
* @author Ever Conde
* @version 1.0 04/03/2026
*/

public class Ejercicio1Cronometro {

    private long inicia;
    private long finaliza;

    public Ejercicio1Cronometro() {
        this.inicia = System.currentTimeMillis();
    }

    public long getInicia() {
        return inicia;
    }

    public long getFinaliza() {
        return finaliza;
    }

    public void inicia() {
        this.inicia = System.currentTimeMillis();
    }

    public void detener() {
        this.finaliza = System.currentTimeMillis();
    }

    public long lapsoDeTiempo() {
        return finaliza - inicia;
    }
}
