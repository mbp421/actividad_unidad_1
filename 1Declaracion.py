from dataclasses import dataclass
# 1 declaracion
@dataclass
class Estudiante:
    nombre: str
    edad: int
    promedio: float

# 2 iniciacion
e1 = Estudiante("moises", 25, 9.0)
e2 = Estudiante("rafael", 22, 8.5)
e3 = Estudiante("camila", 21, 7.8)

# 3 recorrido
estudiantes = [e1, e2, e3]

for e in estudiantes:
    print(e.nombre, e.edad, e.promedio)

# 4 modificacion
estudiantes[1].promedio = 9.2  # Cambiar promedio de Luis
