# index() te dice la POSICIÓN (el "índice") de la primera vez que aparece un elemento en la lista.
# Piensa que es como buscar un libro en una estantería y querer saber en qué número de estante está.
# Si el elemento no está en la lista, da un error.

colores = ["rojo", "verde", "azul", "verde", "amarillo"]
posicion_verde = colores.index("verde")
print(posicion_verde) # 1

# Otro ejemplo con números
puntuaciones = [10, 20, 30, 20, 40]
posicion_treinta = puntuaciones.index(30)
print(posicion_treinta) # 2

# ¿Qué pasa si el elemento no está? (Esto causaría un error ValueError)
posicion_naranja = colores.index("naranja")
print(posicion_naranja)