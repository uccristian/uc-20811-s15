# reversed() es como leer una lista desde el final hacia el principio.
# Imagina que tienes una fila de personas y quieres llamarlas en orden inverso.
# reversed() te da esa secuencia, pero no cambia la fila original.
# Si quieres guardar esa secuencia inversa en una nueva lista, tienes que pedirle que la convierta.

numeros = [1, 2, 3, 4, 5]

# Usamos reversed() para empezar a "leer" la lista de atrás hacia adelante.
# Piensa que esto nos da una "receta" para obtener los elementos en orden inverso.
orden_inverso_receta = reversed(numeros)

# Para ver los números en ese orden inverso y guardarlos en una nueva lista,
# necesitamos usar list() para "cocinar" esa receta y crear la lista.
nueva_lista_invertida = list(orden_inverso_receta)
print(nueva_lista_invertida) # [5, 4, 3, 2, 1]

# ¡Importante! La lista original NO ha cambiado. Sigue igual.
print(numeros) # [1, 2, 3, 4, 5]
