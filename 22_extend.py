# extend() es un método que NO existe para las tuplas.
# Al igual que append(), extend() intentaría añadir elementos a la tupla,
# lo que significaría cambiar su tamaño y contenido.
# Como las tuplas son inmutables, no permiten este tipo de modificación directa.

# Como las tuplas son inmutables y no tienen un método 'extend()',
# si necesitas añadir todos los elementos de otra secuencia a una tupla,
# la forma más común es convertir la tupla a una lista, usar 'extend()' en la lista,
# y luego convertir la lista resultante de nuevo a una tupla.

mi_tupla_inicial = (1, 2)
mi_lista_para_modificar = list(mi_tupla_inicial)
print(mi_lista_para_modificar) # [1, 2]

elementos_extras = [3, 4, 5]

mi_lista_para_modificar.extend(elementos_extras)
print(mi_lista_para_modificar) # [1, 2, 3, 4, 5]

nueva_tupla_extendida = tuple(mi_lista_para_modificar)
print(nueva_tupla_extendida) # Nueva tupla extendida: (1, 2, 3, 4, 5)

# La tupla original permanece sin cambios
print(mi_tupla_inicial) # Tupla original (sin cambios): (1, 2)
