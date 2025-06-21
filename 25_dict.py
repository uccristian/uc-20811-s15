# Un dict (diccionario) en Python es una colección de pares 
# clave-valor. Imagina que es como un directorio telefónico 
# donde cada nombre (la clave) está asociado a un número 
# de teléfono (el valor).

# 1. Crear un diccionario llamado 'info_libro'
info_libro = {
    "titulo": "El Principito",
    "autor": "Antoine de Saint-Exupéry",
    "año_publicacion": 1943,
    "genero": "Fábula"
}

# 2. Acceder al título del libro
titulo = info_libro["titulo"]
print(f"El título del libro es: {titulo}")

# 3. Acceder al autor del libro
autor = info_libro["autor"]
print(f"El autor del libro es: {autor}")

# 4. Añadir una nueva pieza de información (una clave y su valor)
info_libro["idioma_original"] = "Francés"
print("Después de añadir el idioma original:", info_libro)

# 5. Modificar un valor existente (cambiar el género)
info_libro["genero"] = "Literatura infantil"
print("Después de modificar el género:", info_libro)