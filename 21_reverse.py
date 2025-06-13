# reverse() es un método que NO existe para las tuplas.
# Al igual que append(), reverse() intentaría cambiar la tupla "en su lugar" (modificarla directamente).
# Dado que las tuplas son inmutables y no se pueden modificar una vez creadas,
# este método no está disponible para ellas.

# Como las tuplas son inmutables, no tienen un método 'reverse()'.
# Para obtener una tupla con los elementos en orden inverso,
# podemos convertirla a una lista, invertir la lista, y luego convertirla de nuevo a tupla.

mi_tupla = (1, 2, 3, 4, 5)
mi_lista = list(mi_tupla)
print(mi_lista) # [1, 2, 3, 4, 5]

mi_lista.reverse()
print(mi_lista) # [5, 4, 3, 2, 1]

nueva_tupla_invertida = tuple(mi_lista)
print(nueva_tupla_invertida) # (5, 4, 3, 2, 1)

# La tupla original permanece sin cambios
print(mi_tupla) # Tupla original (sin cambios): (1, 2, 3, 4, 5)
