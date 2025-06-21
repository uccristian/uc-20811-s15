# El método get() es una forma segura y útil de acceder a los
#  valores en un diccionario. Es una alternativa a la forma 
# tradicional de acceder con corchetes [], y ofrece una ventaja 
# importante.

# ¿Para qué sirve o qué hace?
# Acceso seguro a valores: La función principal de get() es 
# permitirte obtener el valor asociado a una clave específica.
# Manejo de claves inexistentes: Su mayor beneficio es que, si 
# la clave que estás buscando no existe en el diccionario, get() 
# no generará un error (un KeyError). En su lugar, te devolverá 
# un valor por defecto que tú puedes especificar, o None si no 
# especificas ninguno. Esto lo hace muy útil para evitar que tu 
# programa se detenga si una clave no se encuentra.

# Nuestro diccionario de información de libros
info_libro = {
    "titulo": "El Principito",
    "autor": "Antoine de Saint-Exupéry",
    "año_publicacion": 1943
}

print("Diccionario actual:", info_libro)

# --- Caso 1: La clave EXISTE ---
# Obtener el título usando get()
titulo = info_libro.get("titulo")
print(f"\nUsando get() para 'titulo': {titulo}")

# Obtener el autor usando get()
autor = info_libro.get("autor")
print(f"Usando get() para 'autor': {autor}")

# --- Caso 2: La clave NO EXISTE (sin valor por defecto) ---
# Intentar obtener el 'idioma' (no existe en nuestro diccionario)
idioma = info_libro.get("idioma")
print(f"\nUsando get() para 'idioma' (no existe): {idioma}") # Esto imprimirá None

# --- Caso 3: La clave NO EXISTE (con valor por defecto) ---
# Intentar obtener el 'genero', y si no existe, que diga 'Desconocido'
genero = info_libro.get("genero", "Desconocido")
print(f"\nUsando get() para 'genero' (con valor por defecto): {genero}")

# Ahora, ¿qué pasa si la clave 'genero' sí existiera?
info_libro["genero"] = "Fábula"
genero_existente = info_libro.get("genero", "Desconocido")
print(f"Si 'genero' existe ahora: {genero_existente}")
