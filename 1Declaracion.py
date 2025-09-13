from dataclasses import dataclass

# 1. Declaración
@dataclass
class Estudiante:
    nombre: str
    edad: int
    promedio: float

# 2. Iniciación
e1 = Estudiante("moises", 25, 5.0)
e2 = Estudiante("rafael", 22, 4.5)
e3 = Estudiante("camila", 21, 3.8)

# 3. Recorrido inicial
estudiantes = [e1, e2, e3]

print("--- Datos antes de la modificación ---")
for e in estudiantes:
    
    print(f"Nombre: {e.nombre}, Edad: {e.edad}, Promedio: {e.promedio}")

# 4. Modificación

estudiantes[0].promedio = 4.2

# 5. Recorrido para mostrar la modificación
print("\n--- Datos después de la modificación ---")
for e in estudiantes:

    print(f"Nombre: {e.nombre}, Edad: {e.edad}, Promedio: {e.promedio}")