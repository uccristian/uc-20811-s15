# El método clear() es el más sencillo de todos los métodos de 
# eliminación de diccionarios. Su propósito es simplemente vaciar 
# por completo un diccionario, eliminando todos sus pares clave-valor 
# y dejándolo como un diccionario vacío. Piensa en él como si 
# estuvieras pulsando el botón de "borrar todo" en una pizarra, 
# dejándola completamente limpia.

# ¿Para qué sirve o qué hace?
# Vaciar un diccionario: Su única función es remover todos los 
# elementos de un diccionario, dejando una estructura de diccionario 
# vacía lista para ser rellenada de nuevo, o simplemente para liberar
#  la memoria que ocupaba.

# Nuestro diccionario de invitados: nombre y estado de confirmación
lista_invitados = {
    "Carlos Rodriguez": "Confirmado",
    "Laura Martinez": "Pendiente",
    "Sofia Diaz": "Confirmado",
    "Roberto Jimenez": "Ausente"
}

print("Lista de invitados inicial:", lista_invitados)
print(f"Número de invitados: {len(lista_invitados)}") # len() nos dice cuántos elementos tiene

# --- Usando clear() para vaciar la lista de invitados ---
print("\n--- Vaciando la lista de invitados con clear() ---")
lista_invitados.clear()

print("Lista de invitados después de clear():", lista_invitados)
print(f"Número de invitados después de clear(): {len(lista_invitados)}")

# --- Demostración en un diccionario ya vacío ---
print("\n--- Intentando limpiar un diccionario ya vacío ---")
otro_diccionario_vacio = {}
print("Otro diccionario (ya vacío):", otro_diccionario_vacio)
otro_diccionario_vacio.clear() # No hace nada, pero tampoco da error
print("Otro diccionario después de clear() (sigue vacío):", otro_diccionario_vacio)