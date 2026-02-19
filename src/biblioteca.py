import json
import os

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
    def __init__(self, archivo="libros.json"):
        self.libros = {}
        self.usuarios = {}
        self.archivo = archivo
        self.cargar_libros()

    # ---------------- Guardar / Cargar ----------------
    def guardar_libros(self):
        datos = {
            id: {
                "titulo": l.titulo,
                "autor": l.autor,
                "disponible": l.disponible
            }
            for id, l in self.libros.items()
        }
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

    def cargar_libros(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                for id, info in datos.items():
                    libro = Libro(id, info["titulo"], info["autor"])
                    libro.disponible = info.get("disponible", True)
                    self.libros[id] = libro

    # ---------------- Funcionalidad básica ----------------
    def agregar_libro(self, libro):
        self.libros[libro.id] = libro
        self.guardar_libros()

    def listar_libros(self):
        return list(self.libros.values())

    def prestar_libro(self, libro_id):
        libro = self.libros.get(libro_id)
        if libro and libro.disponible:
            libro.disponible = False
            self.guardar_libros()
            return True
        return False

    def devolver_libro(self, libro_id):
        libro = self.libros.get(libro_id)
        if libro and not libro.disponible:
            libro.disponible = True
            self.guardar_libros()
            return True
        return False

    # ---------------- Métodos de búsqueda ----------------
    def buscar_libro_por_id(self, libro_id):
        return self.libros.get(libro_id)

    def buscar_libro_por_titulo(self, titulo):
        for libro in self.libros.values():
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def buscar_libro_por_titulo_parcial(self, texto):
        return [
            libro for libro in self.libros.values()
            if texto.lower() in libro.titulo.lower()
        ]

    def buscar_libro_por_autor(self, autor):
        return [
            libro for libro in self.libros.values()
            if libro.autor.lower() == autor.lower()
        ]

