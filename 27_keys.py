# El método keys() te permite obtener una vista de todas las claves 
# que existen en un diccionario. Piensa en él como una forma de 
# pedirle al diccionario que te muestre solo los "nombres" de los 
# elementos que contiene.

# ¿Para qué sirve o qué hace?
# Obtener todas las claves: Su propósito principal es darte un objeto
#  que representa todas las claves que están actualmente en el 
# diccionario.
# Iterar sobre las claves: Es muy útil cuando necesitas recorrer 
# cada una de las claves de un diccionario para hacer algo con 
# ellas o con sus valores asociados.
# Verificar la existencia de claves: Aunque get() o in son más 
# comunes para esto, keys() te da una colección con la que puedes 
# verificar si una clave específica está presente 
# (aunque no es su uso más eficiente).

# Nuestro diccionario de información de libros
info_libro = {
    "titulo": "El Principito",
    "autor": "Antoine de Saint-Exupéry",
    "año_publicacion": 1943,
    "genero": "Fábula"
}

print("Diccionario actual:", info_libro)

# --- Usando keys() para obtener las claves ---
# Obtener el objeto dict_keys
claves_libro = info_libro.keys()
print(f"\nEl objeto keys() es: {claves_libro}") # Verás un objeto dict_keys

# --- Iterar sobre las claves ---
print("\nRecorriendo las claves del libro:")
for clave in claves_libro:
    print(f"- {clave}")

# --- Acceder a los valores usando las claves obtenidas ---
print("\nClave y su valor correspondiente:")
for clave in claves_libro:
    valor = info_libro[clave] # Accedemos al valor usando la clave
    print(f"- {clave}: {valor}")
