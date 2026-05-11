# a) Clase Biblioteca: Representa la biblioteca universitaria.
class Biblioteca:
    # • Métodos: Constructor que reciba el nombre.
    def __init__(self, nombre, dias, hora_ap, hora_ci):
        # • Atributos: Nombre de la biblioteca, Listas de libros, autores y préstamos
        self.__nombre = nombre
        self.__libros = []
        self.__autores = []
        self.__prestamos = []
        # • Atributo: Horario de atención (como clase interna)
        self.__horario = Horario(dias, hora_ap, hora_ci)

    # ◦ agregarLibro(Libro libro): Agrega un libro existente.
    def agregarLibro(self, libro):

        # b) RELACIÓN DE AGREGACIÓN. 
        # Biblioteca- Libro: 

        self.__libros.append(libro)

    # ◦ agregarAutor(Autor autor): Registra un autor existente.
    def agregarAutor(self, autor):

        # b) RELACIÓN DE AGREGACIÓN. 
        # Biblioteca- Autor:

        self.__autores.append(autor)

    # ◦ prestarLibro(Estudiante estudiante, Libro libro): Crea un préstamo.
    def prestarLibro(self, estudiante, libro, f_prestamo, f_devolucion):
        nuevo_prestamo = Prestamo(f_prestamo, f_devolucion, estudiante, libro)
        self.__prestamos.append(nuevo_prestamo)
        return nuevo_prestamo

    # ◦ mostrarEstado(): Muestra el estado completo de la biblioteca.
    def mostrarEstado(self):
        print(f"\n ESTADO DE LA BIBLIOTECA: {self.__nombre} ")
        self.__horario.mostrarHorario()
        print(f"Libros: {len(self.__libros)} | Autores: {len(self.__autores)} | Préstamos activos: {len(self.__prestamos)}")
        for p in self.__prestamos:
            p.mostrarInfo()

    # ◦ cerrarBiblioteca(): Cierra la biblioteca (mensaje) y dejan de existir los préstamos.
    def cerrarBiblioteca(self):
        print(f"\nCerrando la biblioteca '{self.__nombre}'...")
        self.__prestamos.clear()
        print("Los prestamos han dejado de existir.")


# b) Clase Libro: Representa un libro físico.
class Libro:
    # • Métodos: Constructor que reciba título, ISBN y contenido de páginas
    def __init__(self, titulo, isbn, contenidos_paginas):
        # • Atributos: Título, ISBN
        self.__titulo = titulo
        self.__isbn = isbn
        
        # • Atributos: Páginas (como clases internas)
        self.__paginas = []

        # a) RELACIÓN DE COMPOSICIÓN. 
        for i, contenido in enumerate(contenidos_paginas):
            self.__paginas.append(Pagina(i + 1, contenido))

    def get_titulo(self):
        return self.__titulo

    # ◦ leer(): Muestra todas las páginas del libro.
    def leer(self):
        print(f"\nLeyendo libro: {self.__titulo}")
        for pagina in self.__paginas:
            pagina.mostrarPagina()


# c) Clase Autor: Representa al escritor de los libros.
class Autor:
    # • Métodos: Constructor que reciba nombre, nacionalidad.
    def __init__(self, nombre, nacionalidad):
        # • Atributos: Nombre, Nacionalidad.
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad

    # ◦ mostrarInfo(): Muestra los datos del autor.
    def mostrarInfo(self):
        print(f"Autor: {self.__nombre} ({self.__nacionalidad})")


# d) Clase Estudiante: Representa a los usuarios de la biblioteca.
class Estudiante:
    # • Métodos: Constructor que reciba código y nombre.
    def __init__(self, codigo_estudiante, nombre):
        # • Atributos: Código de estudiante, Nombre.
        self.__codigo = codigo_estudiante
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    # ◦ mostrarInfo(): Muestra los datos del estudiante.
    def mostrarInfo(self):
        print(f"Estudiante: {self.__nombre} (Cód: {self.__codigo})")


# e) Clase Prestamo: Representa el préstamo de un libro a un estudiante.
class Prestamo:
    # • Métodos: Constructor que reciba estudiante y libro. (Se añaden fechas por lógica de atributos)
    def __init__(self, fecha_prestamo, fecha_devolucion, estudiante, libro):
        # • Atributos: Fecha de préstamo, Fecha de devolución.
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = fecha_devolucion

        # Especificaciones: c) RELACIÓN DE ASOCIACIÓN. 
        # Prestamo- Estudiante: 
        # Prestamo- Libro:
        # • Atributos: Referencias al estudiante y libro.

        self.__estudiante = estudiante
        self.__libro = libro

    # ◦ mostrarInfo(): Muestra detalles del préstamo.
    def mostrarInfo(self):
        print(f" -> Prestamo activo: '{self.__libro.get_titulo()}' a nombre de {self.__estudiante.get_nombre()}")


# f) Clase Horario: Representa el horario de atención para el lector.
class Horario:
    # • Métodos: Constructor que reciba días de apertura, hora de apertura, hora de cierre.
    def __init__(self, dias_apertura, hora_apertura, hora_cierre):
        # • Atributos: Días de apertura, Hora de apertura, Hora de cierre.
        self.__dias = dias_apertura
        self.__hora_ap = hora_apertura
        self.__hora_ci = hora_cierre

    # ◦ mostrarHorario(): Muestra el horario de atención.
    def mostrarHorario(self):
        print(f"Horario: {self.__dias} de {self.__hora_ap} a {self.__hora_ci}")


# g) Clase Página: Representa una página física del libro.
class Pagina:
    # • Métodos: Constructor que reciba número de la página, contenido de la página.
    def __init__(self, numero_pagina, contenido):
        # • Atributos: Número de página, Contenido de la página.
        self.__numero = numero_pagina
        self.__contenido = contenido

    # ◦ mostrarHorario(): Muestra el horario de atención. 
    def mostrarPagina(self):
        print(f" [Pág. {self.__numero}] {self.__contenido}")