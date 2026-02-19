import pytest
from src.biblioteca import Libro, Usuario, Biblioteca

# ---------------- TESTS BÁSICOS ----------------

def test_agregar_libro_y_listar():
    biblioteca = Biblioteca()
    libro = Libro(1, "1984", "George Orwell")
    biblioteca.agregar_libro(libro)

    libros = biblioteca.listar_libros()
    assert len(libros) == 1
    assert libros[0].titulo == "1984"


def test_prestar_y_devolver_libro():
    biblioteca = Biblioteca()
    libro = Libro(1, "1984", "George Orwell")
    biblioteca.agregar_libro(libro)

    assert biblioteca.prestar_libro(1) is True
    assert libro.disponible is False
    assert biblioteca.devolver_libro(1) is True
    assert libro.disponible is True

# ---------------- TESTS DE BÚSQUEDA ----------------

def test_buscar_libro_por_id():
    biblioteca = Biblioteca()
    libro = Libro(1, "1984", "George Orwell")
    biblioteca.agregar_libro(libro)

    resultado = biblioteca.buscar_libro_por_id(1)
    assert resultado is not None
    assert resultado.titulo == "1984"

def test_buscar_libro_por_titulo():
    biblioteca = Biblioteca()
    libro = Libro(1, "1984", "George Orwell")
    biblioteca.agregar_libro(libro)

    resultado = biblioteca.buscar_libro_por_titulo("1984")
    assert resultado is not None
    assert resultado.autor == "George Orwell"

def test_buscar_libro_inexistente():
    biblioteca = Biblioteca()
    resultado = biblioteca.buscar_libro_por_id(999)
    assert resultado is None

# ---------------- TESTS DE BÚSQUEDA AVANZADA ----------------

def test_buscar_libro_por_titulo_parcial():
    biblioteca = Biblioteca()
    libro1 = Libro(1, "1984", "George Orwell")
    libro2 = Libro(2, "Animal Farm", "George Orwell")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    parciales = biblioteca.buscar_libro_por_titulo_parcial("Ani")
    assert len(parciales) == 1
    assert parciales[0].titulo == "Animal Farm"

def test_buscar_libro_por_autor():
    biblioteca = Biblioteca()
    libro1 = Libro(1, "1984", "George Orwell")
    libro2 = Libro(2, "Animal Farm", "George Orwell")
    libro3 = Libro(3, "Brave New World", "Aldous Huxley")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    resultados = biblioteca.buscar_libro_por_autor("George Orwell")
    assert len(resultados) == 2
    titulos = [l.titulo for l in resultados]
    assert "1984" in titulos
    assert "Animal Farm" in titulos
