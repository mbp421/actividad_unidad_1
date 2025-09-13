class Estudiante:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    def mostrarInfo(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Promedio: {self.promedio}")

    def setPromedio(self, nuevo_promedio):
        self.promedio = nuevo_promedio

# 2 Inicialización
e1 = Estudiante("Moisés", 25, 4.0)
e2 = Estudiante("Rafael", 22, 4.5)
e3 = Estudiante("Camila", 21, 3.8)
estudiantes = [e1, e2, e3]

# 3 Recorrido
print("--- Lista de estudiantes original ---")
for e in estudiantes:
    e.mostrarInfo()

# 4 Modificación
e2.setPromedio(4.1)

print("\n--- Lista de estudiantes después de la modificación ---")
for e in estudiantes:
    e.mostrarInfo()