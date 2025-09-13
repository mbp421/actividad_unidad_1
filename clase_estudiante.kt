// 1 Declaración
class Estudiante(var nombre: String, var edad: Int, var promedio: Double) {

    fun mostrarInfo() {
        println("Nombre: $nombre, Edad: $edad, Promedio: $promedio")
    }

}

fun main() {
    // 2 Inicialización
    val e1 = Estudiante("Moisés", 25, 4.0)
    val e2 = Estudiante("Rafael", 22, 4.5)
    val e3 = Estudiante("Camila", 21, 3.8)
    val estudiantes = listOf(e1, e2, e3)

    // 3 Recorrido
    println("--- Lista de estudiantes original ---")
    estudiantes.forEach { it.mostrarInfo() }

    // 4 Modificación
    e2.promedio = 5.0

    println("\n--- Lista de estudiantes después de la modificación ---")
    estudiantes.forEach { it.mostrarInfo() }
}