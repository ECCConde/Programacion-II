from GestionBiblioteca import Biblioteca, Libro, Autor, Estudiante

if __name__ == "__main__":
    
    #  RELACION DE COMPOSICION 
    biblioteca_central = Biblioteca("Biblioteca Central UMSA", "Lunes a Viernes", "08:00", "20:00")

    # RELACION DE COMPOSICION (Libro - Página)
    libro_poo = Libro("Programacion Orientada a Objetos", "978-12345", [
        "Introduccion a UML y diagramas de clases.",
        "Conceptos profundos de Asociacion, Agregacion y Composicion."
    ])
    
    autor_felipez = Autor("Lic. Jhonny Felipez", "Boliviano")
    estudiante_u = Estudiante("1002345", "Ever")


    # RELACION DE AGREGACION
    biblioteca_central.agregarAutor(autor_felipez)
    biblioteca_central.agregarLibro(libro_poo)


    # RELACION DE ASOCIACION
    biblioteca_central.prestarLibro(estudiante_u, libro_poo, "16/04/2026", "23/04/2026")


    #  Resto de las operaciones para mostrar resultados 
    print("\n. informacion de la biblioteca.")
    biblioteca_central.mostrarEstado()

    print("\n. Mostrando informacion del libro.")
    libro_poo.leer()

    print("\n. Cerrando la biblioteca.")
    biblioteca_central.cerrarBiblioteca()

    print("\n. despues del cierre.")
    
    if libro_poo is not None and estudiante_u is not None:
        print(f"Objeto Estudiante: {estudiante_u.get_nombre()} - Sigue existiendo.")
        print(f"Objeto Libro: {libro_poo.get_titulo()} - Sigue existiendo.")
        print("Objeto Autor:", end=" ") 
        autor_felipez.mostrarInfo()
        print(" Sigue existiendo.")