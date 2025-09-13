// se solicita que se eliminen los nuemros duplicados
// solo se deven mostrar los numeros unicos
fun eliminarDuplicados(lista: List<Int>): List<Int> {
    val unicos = lista.toSet()

    return unicos.toList()
}

fun main() {
    val numerosConDuplicados = listOf(2, 3, 4, 3, 2, 2, 1)
    val numerosUnicos = eliminarDuplicados(numerosConDuplicados)
    println(numerosUnicos) 
}