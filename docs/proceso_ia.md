                            
                         Cambios realizados por mí

Simplifiqué las historias para que fueran más claras y directas.

Eliminé funcionalidades avanzadas (como reservas online o multas) porque el proyecto es de nivel básico.

Ajusté el diagrama de flujo para que coincida exactamente con los métodos implementados en mi clase Biblioteca.

Adapté las historias para que reflejen las funciones reales del sistema (agregar, buscar, prestar y devolver libros).


 
                    Que se refactorizo en el codigo mediante IA.

En resumen técnico
Refactoricé tu proyecto aplicando:
✔ Principio de Responsabilidad Única (SRP)
✔ Eliminación de código duplicado
✔ Separación por capas
✔ Encapsulamiento
✔ Mejor manejo de errores
✔ Mejor organización de carpetas
✔ Código más mantenible y escalable

Nivel del proyecto
Antes:
Proyecto funcional pero con errores estructurales.
Ahora:
Proyecto estructurado a nivel intermedio-profesional listo para:
✔Evaluación académica
✔Defender en presentación
✔Escalar a API
✔Agregar tests unitarios


1️⃣ Elimino clases duplicadas
❌ Antes
Tenías dos clases Biblioteca en el mismo archivo.
Problema:
La segunda sobrescribía a la primera.
Generaba errores como:
AttributeError: listar_libros
AttributeError: cargar_libros

✅ Ahora
Existe una sola clase Biblioteca, limpia y organizada.
✔ Se eliminaron conflictos
✔ Se eliminaron métodos repetidos
✔ Se corrigió la estructura


2️⃣ Separación de responsabilidades (Principio SRP)
❌ Antes
Todo estaba mezclado en un mismo archivo:
-Modelo (Libro)
-Usuario
-Lógica de negocio
-Persistencia (JSON)
-GUI
Esto rompe el principio de responsabilidad única.

✅ Ahora
Separé el proyecto en capas:

📁 models/
Contiene solo las entidades:
Libro
Usuario
👉 Solo representan datos.

📁 services/
Contiene:
Biblioteca
👉 Maneja:
Lógica de negocio
Persistencia
Validaciones

📁 gui/
Contiene:
BibliotecaGUI
👉 Solo maneja interfaz gráfica.


3️⃣ Elimino código duplicado
En tu archivo original tenías métodos repetidos como:
buscar_libro_por_id
buscar_libro_por_titulo
buscar_libro_por_autor
Aparecían dos veces.

Ahora:
✔ Cada método existe una sola vez
✔ No hay redefiniciones innecesarias


4️⃣ Mejoré la persistencia
❌ Antes
Guardado y carga estaban mezclados con lógica
No había encapsulamiento

✅ Ahora
Se crearon métodos privados:
_guardar()
_cargar()

✔ Encapsulamiento mejorado
✔ Persistencia aislada
✔ Código más limpio


5️⃣ Mejor manejo de errores
❌ Antes
prestar_libro() devolvía solo True o False.
No sabías el motivo del error.

✅ Ahora
Devuelve:
(True, "Préstamo exitoso")
(False, "Libro no encontrado")
(False, "Libro ya prestado")

✔ Mejor comunicación con la GUI
✔ Más profesional
✔ Escalable


6️⃣ Conversión de objetos a JSON correctamente
Antes guardabas datos manualmente.

Ahora agregué en Libro:
def to_dict()
@staticmethod
def from_dict()

✔ Modelo sabe convertirse a JSON
✔ Mejor diseño orientado a objetos
✔ Más limpio y reutilizable


7️⃣ Organización profesional del proyecto
Antes:
todo en src/

Ahora:
models/
services/
gui/
data/
docs/
main.py

✔ Arquitectura más profesional
✔ Más fácil de mantener
✔ Más fácil de escalar


8️⃣ Limpieza de imports
Antes:
requests importado donde no se usaba
sys.path.append innecesario

Ahora:
✔ Cada archivo importa solo lo que necesita
✔ No hay hacks de rutas


9️⃣ Mejor diseño orientado a objetos
Antes:
ID podía ser int o str sin control
Sin validación de duplicados


Ahora:
ID convertido siempre a string
Validación al agregar libro
Uso de excepciones controladas


