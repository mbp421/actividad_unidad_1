# se solicita que se eliminen los nuemros duplicados
# solo se deven mostrar los numeros unicos
def eliminar_duplicados(A: list[int]) -> list[int]:
    unicos = set(A)
    return [num for num in unicos]

print(eliminar_duplicados([2,3,4,3,2,2,1]))