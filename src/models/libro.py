class Libro:
    def __init__(self, id, titulo, autor, disponible=True):
        self.id = str(id)
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "disponible": self.disponible
        }

    @staticmethod
    def from_dict(id, data):
        return Libro(
            id=id,
            titulo=data["titulo"],
            autor=data["autor"],
            disponible=data.get("disponible", True)
        )

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({estado})"