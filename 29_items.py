# El método items() es como una combinación de keys() y values(). 
# Te permite obtener una vista de todos los pares clave-valor que 
# contiene un diccionario. Imagina que es como pedirle al diccionario 
# que te muestre su contenido completo, mostrando tanto el "nombre" 
# como el "valor" de cada entrada.

# ¿Para qué sirve o qué hace?
# Obtener pares clave-valor: Su función principal es darte un objeto 
# que representa todos los elementos del diccionario, donde cada 
# elemento es una tupla que contiene una clave y su valor 
# correspondiente (clave, valor).
# Iterar de forma eficiente: Es ideal cuando necesitas recorrer el 
# diccionario y trabajar tanto con la clave como con el valor de 
# cada elemento a la vez. Esto es muy común cuando quieres mostrar 
# o procesar toda la información de un diccionario.
# Acceso completo a los datos: Te proporciona una forma conveniente 
# de ver y manejar la estructura completa del diccionario.

# Nuestro diccionario de información de libros
info_libro = {
    "titulo": "El Principito",
    "autor": "Antoine de Saint-Exupéry",
    "año_publicacion": 1943,
    "genero": "Fábula"
}

print("Diccionario actual:", info_libro)

# --- Usando items() para obtener los pares clave-valor ---
# Obtener el objeto dict_items
items_libro = info_libro.items()
print(f"\nEl objeto items() es: {items_libro}") # Verás un objeto dict_items con tuplas

# --- Iterar sobre los pares clave-valor ---
print("\nRecorriendo el diccionario con items():")
for clave, valor in items_libro: # Aquí desempaquetamos la tupla directamente
    print(f"- {clave}: {valor}")
