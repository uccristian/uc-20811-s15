# del elimina elementos de una lista usando su índice o para eliminar la lista completa.

colores = ["rojo", "verde", "azul", "amarillo"]
del colores[1]
print(colores) # ['rojo', 'azul', 'amarillo']

# Eliminar un rango de elementos (del índice 0 al 1, sin incluir el 2)
numeros = [10, 20, 30, 40, 50]
del numeros[0:2] # Elimina 10 y 20
print(numeros) # [30, 40, 50]

# También puedes eliminar la lista completa (la variable dejaría de existir)
# del colores
# print(colores) # Esto daría un error si intentas imprimirla después de eliminarla