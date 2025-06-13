# clear() es un método que NO existe para las tuplas.
# Su propósito es eliminar todos los elementos de una colección, dejándola vacía.
# Sin embargo, las tuplas son inmutables, lo que significa que su contenido y tamaño
# no pueden ser modificados una vez creadas. Por lo tanto, no se pueden "vaciar" directamente.

# Como las tuplas son inmutables, no tienen un método 'clear()' para vaciarlas.
# Si necesitas una tupla "vacía" a partir de una existente (o una nueva tupla vacía),
# puedes usar la estrategia de convertirla a lista, usar 'clear()' en la lista,
# y luego convertir la lista vacía de nuevo a tupla.

mi_tupla = (1, 2, 3, 4, 5)
mi_lista = list(mi_tupla)
print(mi_lista) # [1, 2, 3, 4, 5]

mi_lista.clear()
print(mi_lista) # []

nueva_tupla_vacia = tuple(mi_lista)
print(nueva_tupla_vacia) # ()

# La tupla original permanece sin cambios
print(mi_tupla) # (1, 2, 3, 4, 5)
