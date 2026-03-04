/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejercicio1;

/**
 *
 * @author Ever
 */
public class Cronometro {

    private int inicia;
    private int finaliza;

    public Cronometro() {
        this.inicia = (int) System.currentTimeMillis();
    }

    public long getInicia() {
        return inicia;
    }

    public long getFinaliza() {
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