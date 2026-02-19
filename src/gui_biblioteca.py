import tkinter as tk
from tkinter import messagebox, simpledialog
from biblioteca import Biblioteca, Libro
import requests
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class BibliotecaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca Talento Solutions")
        self.biblioteca = Biblioteca()

        # Lista de libros
        self.lista_libros = tk.Listbox(root, width=50)
        self.lista_libros.pack(pady=10)

        # Botones
        tk.Button(root, text="Agregar Libro", command=self.agregar_libro).pack(fill='x')
        tk.Button(root, text="Prestar Libro", command=self.prestar_libro).pack(fill='x')
        tk.Button(root, text="Devolver Libro", command=self.devolver_libro).pack(fill='x')
        tk.Button(root, text="Buscar Libro Local", command=self.buscar_libro_local).pack(fill='x')
        tk.Button(root, text="Buscar Libros Públicos", command=self.buscar_libros_publicos).pack(fill='x')
        tk.Button(root, text="Actualizar Lista", command=self.actualizar_lista).pack(fill='x')

        self.actualizar_lista()

    # ---------------- Funciones de la GUI ----------------
    def actualizar_lista(self):
        self.lista_libros.delete(0, tk.END)
        for libro in self.biblioteca.listar_libros():
            estado = "Disponible" if libro.disponible else "Prestado"
            self.lista_libros.insert(tk.END, f"{libro.id}: {libro.titulo} - {libro.autor} ({estado})")

    def agregar_libro(self):
        id_libro = simpledialog.askstring("ID", "ID del libro:")
        titulo = simpledialog.askstring("Título", "Título del libro:")
        autor = simpledialog.askstring("Autor", "Autor del libro:")
        if id_libro and titulo and autor:
            libro = Libro(id_libro, titulo, autor)
            self.biblioteca.agregar_libro(libro)
            self.actualizar_lista()
            messagebox.showinfo("Éxito", "Libro agregado correctamente.")

    def prestar_libro(self):
        id_libro = simpledialog.askstring("Prestar", "ID del libro a prestar:")
        if self.biblioteca.prestar_libro(id_libro):
            self.actualizar_lista()
            messagebox.showinfo("Éxito", "Libro prestado.")
        else:
            messagebox.showerror("Error", "No se pudo prestar el libro.")

    def devolver_libro(self):
        id_libro = simpledialog.askstring("Devolver", "ID del libro a devolver:")
        if self.biblioteca.devolver_libro(id_libro):
            self.actualizar_lista()
            messagebox.showinfo("Éxito", "Libro devuelto.")
        else:
            messagebox.showerror("Error", "No se pudo devolver el libro.")

    def buscar_libro_local(self):
        titulo = simpledialog.askstring("Buscar local", "Título del libro:")
        libro = self.biblioteca.buscar_libro_por_titulo(titulo)
        if libro:
            estado = "Disponible" if libro.disponible else "Prestado"
            messagebox.showinfo("Libro encontrado", f"{libro.id}: {libro.titulo} - {libro.autor} ({estado})")
        else:
            messagebox.showwarning("No encontrado", "El libro no existe.")

    def buscar_libros_publicos(self):
        titulo = simpledialog.askstring("Buscar público", "Título del libro:")
        if not titulo:
            return
        url = f"https://openlibrary.org/search.json?title={titulo}"
        try:
            response = requests.get(url)
            response.raise_for_status()
        except:
            messagebox.showerror("Error", "No se pudo consultar Open Library.")
            return

        datos = response.json()
        docs = datos.get("docs", [])[:5]
        resultado = ""
        for doc in docs:
            resultado += f"{doc.get('title', 'Sin título')} - {', '.join(doc.get('author_name', ['Desconocido']))}\n"
        if resultado:
            messagebox.showinfo("Resultados Open Library", resultado)
        else:
            messagebox.showinfo("Resultados Open Library", "No se encontraron libros.")

# ---------------- Ejecutar GUI ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaGUI(root)
    root.mainloop()
