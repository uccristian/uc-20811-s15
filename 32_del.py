# La palabra clave del en Python no es un método de diccionario 
# como pop() o popitem(). En cambio, es una declaración (statement) 
# general de Python que se usa para eliminar objetos o partes de 
# objetos de la memoria. Cuando la usas con un diccionario, te 
# permite eliminar un par clave-valor específico.

# Piensa en del como una forma directa de "borrar" algo que ya no
# necesitas.

# ¿Para qué sirve o qué hace?
# Eliminar pares clave-valor de diccionarios: Su uso principal en el
#  contexto de los diccionarios es remover una entrada completa 
# (la clave y su valor asociado) del diccionario.
# Eliminar variables: También puedes usar del para eliminar una 
# variable por completo, lo que la hace inaccesible después de la
#  eliminación.
# Eliminar elementos de listas o tuplas: Aunque no es el tema 
# principal, del también se usa para eliminar elementos en una 
# posición específica de una lista o para eliminar por completo 
# una lista.

# Nuestro diccionario de empleados: nombre y departamento
empleados = {
    "Ana Garcia": "Ventas",
    "Luis Perez": "Marketing",
    "Marta Lopez": "Desarrollo",
    "Pedro Sanchez": "Recursos Humanos"
}

print("Empleados iniciales:", empleados)

# --- Usando del para eliminar un empleado que SÍ existe ---
print("\n--- Eliminando un empleado existente ---")
del empleados["Luis Perez"]
print("Después de eliminar a Luis Perez:", empleados)

# --- Usando del para eliminar otro empleado ---
print("\n--- Eliminando otro empleado ---")
del empleados["Ana Garcia"]
print("Después de eliminar a Ana Garcia:", empleados)

# --- Demostración de KeyError si la clave NO existe ---
print("\n--- Intentando eliminar un empleado que NO existe ---")
try:
    # Esto causará un KeyError porque 'Carlos Ruiz' no está en el diccionario
    del empleados["Carlos Ruiz"]
    print("Después de intentar eliminar a Carlos Ruiz:", empleados)
except KeyError:
    print("¡Error! No se encontró a 'Carlos Ruiz' en la lista de empleados. Se produjo un KeyError.")

print("Empleados al final del ejemplo:", empleados)