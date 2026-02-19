import requests 

# src/biblioteca.py

class Libro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({estado})"


class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    # ---------------- Funcionalidad básica ----------------
    def agregar_libro(self, libro):
        """Agrega un libro a la biblioteca"""
        self.libros[libro.id] = libro

    def registrar_usuario(self, usuario):
        """Registra un usuario en la biblioteca"""
        self.usuarios[usuario.id] = usuario

    def prestar_libro(self, libro_id):
        """Presta un libro si está disponible"""
        libro = self.libros.get(libro_id)
        if libro and libro.disponible:
            libro.disponible = False
            return True
        return False

    def devolver_libro(self, libro_id):
        """Devuelve un libro prestado"""
        libro = self.libros.get(libro_id)
        if libro and not libro.disponible:
            libro.disponible = True
            return True
        return False

       # ---------------- MÉTODO IMPORTANTE QUE FALTABA ----------------
    def listar_libros(self):
        """Devuelve todos los libros en la biblioteca"""
        return list(self.libros.values())

    # Métodos de búsqueda
    def buscar_libro_por_id(self, libro_id):
        return self.libros.get(libro_id)

    def buscar_libro_por_titulo(self, titulo):
        for libro in self.libros.values():
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def buscar_libro_por_titulo_parcial(self, texto):
        return [libro for libro in self.libros.values() if texto.lower() in libro.titulo.lower()]

    def buscar_libro_por_autor(self, autor):
        return [libro for libro in self.libros.values() if libro.autor.lower() == autor.lower()]


    # ---------------- NUEVAS FUNCIONES DE BÚSQUEDA ----------------
    def buscar_libro_por_id(self, libro_id):
        """Devuelve un libro por su ID o None si no existe"""
        return self.libros.get(libro_id)

    def buscar_libro_por_titulo(self, titulo):
        """Devuelve un libro con título exacto (case insensitive)"""
        for libro in self.libros.values():
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def buscar_libro_por_titulo_parcial(self, texto):
        """Devuelve una lista de libros cuyo título contenga el texto (case insensitive)"""
        return [libro for libro in self.libros.values() if texto.lower() in libro.titulo.lower()]

    def buscar_libro_por_autor(self, autor):
        """Devuelve una lista de libros de un autor dado"""
        return [libro for libro in self.libros.values() if libro.autor.lower() == autor.lower()]


# ---------------- Bloque de prueba manual ----------------
if __name__ == "__main__":
    biblioteca = Biblioteca()
    libro1 = Libro(1, "1984", "George Orwell")
    libro2 = Libro(2, "Animal Farm", "George Orwell")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    print("Libros disponibles:")
    for l in biblioteca.listar_libros():
        print(l)

    # prueba búsqueda exacta
    resultado = biblioteca.buscar_libro_por_titulo("1984")
    print("\nBúsqueda exacta por título '1984':")
    print(resultado if resultado else "No encontrado")

    # prueba búsqueda parcial
    parciales = biblioteca.buscar_libro_por_titulo_parcial("Ani")
    print("\nBúsqueda parcial por 'Ani':")
    for l in parciales:
        print(l)

    # búsqueda por autor
    orwell = biblioteca.buscar_libro_por_autor("George Orwell")
    print("\nLibros por George Orwell:")
    for l in orwell:
        print(l)


import json
import os

class Biblioteca:
    def __init__(self, archivo="libros.json"):
        self.libros = {}
        self.usuarios = {}
        self.archivo = archivo
        self.cargar_libros()

    # ---------------- Guardar / Cargar ----------------
    def guardar_libros(self):
        """Guarda los libros en un archivo JSON"""
        datos = {id: {"titulo": l.titulo, "autor": l.autor, "disponible": l.disponible}
                 for id, l in self.libros.items()}
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

    def cargar_libros(self):
        """Carga los libros desde un archivo JSON si existe"""
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                for id, info in datos.items():
                    libro = Libro(id, info["titulo"], info["autor"])
                    libro.disponible = info.get("disponible", True)
                    self.libros[id] = libro

    # ---------------- Métodos existentes ----------------
    def agregar_libro(self, libro):
        self.libros[libro.id] = libro
        self.guardar_libros()  # guardar al agregar

    def prestar_libro(self, libro_id):
        libro = self.libros.get(libro_id)
        if libro and libro.disponible:
            libro.disponible = False
            self.guardar_libros()  # guardar al prestar
            return True
        return False

    def devolver_libro(self, libro_id):
        libro = self.libros.get(libro_id)
        if libro and not libro.disponible:
            libro.disponible = True
            self.guardar_libros()  # guardar al devolver
            return True
        return False
