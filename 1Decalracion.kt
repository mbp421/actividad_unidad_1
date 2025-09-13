// 1 declaracion
data class Estudiante(val nombre: String, val edad: Int, var promedio: Double)

// 2 Iniciacion
val e1 = Estudiante("moises", 25, 9.0)
val e2 = Estudiante("rafael", 22, 8.5)
val e3 = Estudiante("camila", 21, 7.8)

// 3 Recorrido
val estudiantes = listOf(e1, e2, e3)

for (e in estudiantes) {
    println("${e.nombre} - ${e.edad} - ${e.promedio}")
}

// 4 modificacion
estudiantes[1].promedio = 9.2
