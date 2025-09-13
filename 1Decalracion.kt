// 1Decalracion
data class Estudiante(val nombre: String, val edad: Int, var promedio: Double)

fun main() {
    // 2 Inicialización
    val e1 = Estudiante("wendy", 30, 5.0)
    val e2 = Estudiante("Luis", 22, 4.5)
    val e3 = Estudiante("María", 21, 3.8)

    
    val estudiantes = listOf(e1, e2, e3)

    // 3 Recorrido
    println("Lista de estudiantes:")
    for (e in estudiantes) {
        println("${e.nombre} - ${e.edad} - ${e.promedio}")
    }

    // 4 Modificación
    e2.promedio = 4.2
    println("\nDespués de modificar el promedio de ${e2.nombre}:")
    for (e in estudiantes) {
        println("${e.nombre} - ${e.edad} - ${e.promedio}")
    }
}
