# El método values() es el complemento de keys(). Si keys() te da los 
# "nombres" (las claves), values() te da el "contenido" (los valores) 
# almacenados en tu diccionario. Piensa en él como si le pidieras al 
# diccionario que te muestre solo la información o los datos que ha 
# guardado.

# ¿Para qué sirve o qué hace?
# Obtener todos los valores: Su función principal es proporcionarte 
# un objeto que representa todos los valores presentes en el 
# diccionario.
# Iterar sobre los valores: Es extremadamente útil cuando necesitas 
# procesar o examinar cada uno de los datos almacenados, sin 
# preocuparte por sus claves. Por ejemplo, si quieres sumar todos los 
# números que son valores en un diccionario.
# Verificar la existencia de un valor: Puedes usarlo para comprobar 
# si un valor específico ya se encuentra en el diccionario (aunque 
# para esto, a veces es más eficiente iterar directamente o convertir
#  a una lista si la búsqueda es frecuente).


# Nuestro diccionario de información de libros
info_libro = {
    "titulo": "El Principito",
    "autor": "Antoine de Saint-Exupéry",
    "año_publicacion": 1943,
    "genero": "Fábula"
}

print("Diccionario actual:", info_libro)

# --- Usando values() para obtener los valores ---
# Obtener el objeto dict_values
valores_libro = info_libro.values()
print(f"\nEl objeto values() es: {valores_libro}") # Verás un objeto dict_values

# --- Iterar sobre los valores ---
print("\nRecorriendo los valores del libro:")
for valor in valores_libro:
    print(f"- {valor}")

# --- Convertir a una lista de valores (si es necesario) ---
lista_de_valores = list(info_libro.values())
print(f"\nLos valores convertidos a una lista son: {lista_de_valores}")

# Ejemplo de uso: ¿Existe el valor "Antoine de Saint-Exupéry" entre los valores?
if "Antoine de Saint-Exupéry" in valores_libro:
    print("\n'Antoine de Saint-Exupéry' se encuentra entre los valores del diccionario.")