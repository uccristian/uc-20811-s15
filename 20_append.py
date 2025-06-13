# append() es un método que NO existe para las tuplas.
# La razón es que las tuplas son INMUTABLES.
# Una vez que creas una tupla, su tamaño y sus elementos no pueden ser cambiados.
# Añadir un elemento (como hace append()) implicaría cambiar el tamaño de la tupla,
# y eso va en contra de su naturaleza inmutable.

# Como las tuplas son inmutables (no se pueden cambiar directamente),
# un truco común para "modificarlas" es convertirlas primero a una lista,
# hacer los cambios en la lista, y luego convertir la lista de nuevo a una tupla.

mi_tupla = (10, 20, 30)
mi_lista = list(mi_tupla) # [10, 20, 30]

mi_lista.append(40)
print(mi_lista) # [10, 20, 30, 40]

nueva_tupla = tuple(mi_lista)
print(nueva_tupla) # (10, 20, 30, 40)

# La tupla original 'mi_tupla' sigue siendo la misma, sin cambios
print(mi_tupla) # Tupla original (sin cambios): (10, 20, 30)