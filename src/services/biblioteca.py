
import json
import os
from src.models.libro import Libro


class Biblioteca:
    def __init__(self, archivo="data/libros.json"):
        self.archivo = archivo
        self.libros = {}
        self._cargar()

    # ---------------- Persistencia ----------------

    def _guardar(self):
        os.makedirs(os.path.dirname(self.archivo), exist_ok=True)
        datos = {id: libro.to_dict() for id, libro in self.libros.items()}
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

    def _cargar(self):
        if not os.path.exists(self.archivo):
            return
        with open(self.archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            for id, data in datos.items():
                self.libros[id] = Libro.from_dict(id, data)

    # ---------------- CRUD ----------------

    def agregar_libro(self, libro):
        if libro.id in self.libros:
            raise ValueError("El libro ya existe.")
        self.libros[libro.id] = libro
        self._guardar()

    def listar_libros(self):
        return list(self.libros.values())

    def prestar_libro(self, libro_id):
        libro = self.libros.get(libro_id)
        if not libro:
            return False, "Libro no encontrado."
        if not libro.disponible:
            return False, "Libro ya prestado."

        libro.disponible = False
        self._guardar()
        return True, "Préstamo exitoso."

    def devolver_libro(self, libro_id):
        libro = self.libros.get(libro_id)
        if not libro:
            return False, "Libro no encontrado."
        if libro.disponible:
            return False, "El libro ya está disponible."

        libro.disponible = True
        self._guardar()
        return True, "Devolución exitosa."

    # ---------------- Búsquedas ----------------

    def buscar_por_titulo(self, titulo):
        for libro in self.libros.values():
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def buscar_por_autor(self, autor):
        return [
            libro for libro in self.libros.values()
            if libro.autor.lower() == autor.lower()
        ]