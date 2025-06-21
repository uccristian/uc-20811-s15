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

# Porque no reasignar el valor de mi_tupla:
# Rompe la inmutabilidad esperada: Si alguien lee tu código y ve una tupla llamada mi_tupla, espera que su valor no cambie. Si la reasignas, ya no es la tupla original.
# Puede causar bugs: Si usas mi_tupla en otras partes del código esperando el valor original, tendrás resultados inesperados.
# Menos claridad: Es más claro crear una nueva variable para el nuevo valor, así sabes cuál es la original y cuál es la modificada.
# En resumen: reasignar está permitido, pero puede hacer el código menos predecible y más difícil de entender. Por eso, muchas veces es mejor crear una nueva variable