<div align="center">

# Sistema de Gestión de Biblioteca

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![PyTest](https://img.shields.io/badge/Test-pytest-green)](https://pytest.org/)

</div>

---

## Descripción
Solución profesional de gestión de biblioteca en Python: registro de libros, usuarios y operaciones de préstamo/devolución. Arquitectura modular y pruebas automatizadas.

## Objetivos del proyecto
- Implementar un servicio REST/CLI (según alcance) para biblioteca
- Mantener código limpio y modular
- Cubrir responsabilidades con pruebas unitarias
- Brindar UX consistente (por consola o GUI) y manejo de errores

## Estructura del proyecto
- `src/models/` - entidades (Libro, Usuario)
- `src/services/` - lógica de negocio (Biblioteca)
- `src/gui/` - interfaz de usuario
- `tests/` - suite de pruebas
- `data/` - datos de ejemplo (`libros.json`)

## Requisitos
- Python 3.10+
- `pip` disponible

## Instalación
1. Crear entorno virtual (recomendado):
   - `python -m venv venv`
   - `venv\Scripts\activate` (Windows) o `source venv/bin/activate` (Linux/macOS)
2. Instalar dependencias:
   - `pip install -r requirements.txt`

## Ejecución
- Ejecutar aplicación principal:
  - `python main.py`
- Ejecutar interfaz grafica (si aplica):
  - `python -m src.gui.gui_biblioteca`

## Pruebas
- Ejecutar suite:
  - `pytest`

## Buenas prácticas aplicadas
- Código con responsabilidad única
- Separación de capas (modelos, servicios, GUI)
- Manejo de excepciones y validaciones
- Datos de prueba (`test_libros.json`) y fixtures


<div align="center">

## 📜 Licencia

Este proyecto está distribuido bajo la licencia **MIT**.

Puedes usar, modificar y distribuir este software libremente siempre que se incluya la licencia original.

Ver archivo [LICENSE](LICENSE) para más detalles.


## Autor

[![GitHub](https://img.shields.io/badge/GitHub-kindred--98-181717?style=for-the-badge&logo=github)](https://github.com/kindred-98)

---

*Hecho con 🐍 Python y arquitectura limpia*

⭐ Si este proyecto te resulta útil, considera dejarle una estrella en GitHub

</div>