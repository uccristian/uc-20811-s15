# remove() es un método que NO existe para las tuplas.
# Este método intenta eliminar un elemento por su valor, lo que modificaría la tupla.
# Como las tuplas son inmutables, no es posible eliminar elementos directamente de ellas.

# Como las tuplas son inmutables y no tienen un método 'remove()',
# si necesitas "eliminar" un elemento, la forma es crear una *nueva* tupla.
# Esto se logra convirtiendo a lista, usando 'remove()' en la lista,
# y luego convirtiendo la lista resultante de nuevo a tupla.

mi_tupla = ("rojo", "verde", "azul", "verde")
mi_lista = list(mi_tupla)
print(mi_lista) # ['rojo', 'verde', 'azul', 'verde']

mi_lista.remove("verde")
print(mi_lista) # ['rojo', 'azul', 'verde']

nueva_tupla = tuple(mi_lista)
print(nueva_tupla) # ('rojo', 'azul', 'verde')

# La tupla original sigue siendo la misma
print(mi_tupla) # ('rojo', 'verde', 'azul', 'verde')