# El método pop() en los diccionarios te permite eliminar un par 
# clave-valor específico del diccionario y, al mismo tiempo, obtener
#  el valor que estaba asociado a esa clave. Piensa en él como si 
# estuvieras sacando un elemento de una caja (el diccionario), y al
#  hacerlo, no solo lo quitas, sino que también puedes ver qué era 
# lo que sacaste.

# ¿Para qué sirve o qué hace?
# Eliminar por clave y obtener valor: Su función principal es 
# eliminar un elemento del diccionario buscando su clave, y retornar 
# el valor de ese elemento eliminado.
# Gestión de elementos: Es muy útil cuando necesitas procesar un 
# elemento y luego quitarlo del diccionario, por ejemplo, en colas de
#  trabajo o cuando un recurso ha sido utilizado y ya no debe estar 
# disponible.
# Manejo de claves inexistentes de forma segura: Al igual que get(), 
# pop() te permite especificar un valor por defecto si la clave que 
# intentas eliminar no se encuentra. Esto evita que tu programa 
# falle con un KeyError.

# Nuestro diccionario de productos en el carrito: producto y su cantidad
carrito_compras = {
    "manzanas": 5,
    "leche": 2,
    "pan": 1,
    "huevos": 12
}

print("Carrito de compras inicial:", carrito_compras)

# --- Caso 1: Eliminar un producto que SÍ existe (y obtener su cantidad) ---
print("\n--- Eliminando un producto existente ---")
cantidad_manzanas = carrito_compras.pop("manzanas")
print(f"Se eliminaron {cantidad_manzanas} unidades de manzanas.")
print("Carrito después de eliminar manzanas:", carrito_compras)

# --- Caso 2: Intentar eliminar un producto que NO existe (con valor por defecto) ---
print("\n--- Intentando eliminar un producto inexistente con valor por defecto ---")
cantidad_galletas = carrito_compras.pop("galletas", 0) # Si 'galletas' no existe, devuelve 0
print(f"Se intentaron eliminar galletas. Cantidad devuelta: {cantidad_galletas}")
print("Carrito después del intento (no se modificó):", carrito_compras)

# --- Caso 3: Intentar eliminar un producto que NO existe (SIN valor por defecto) ---
print("\n--- Intentando eliminar un producto inexistente SIN valor por defecto ---")
try:
    # Esto causará un KeyError porque 'pizza' no está y no hay valor por defecto
    cantidad_pizza = carrito_compras.pop("pizza")
    print(f"Se eliminó pizza: {cantidad_pizza}")
except KeyError:
    print("¡Error! No se encontró 'pizza' en el carrito. Se produjo un KeyError.")

print("Carrito al final:", carrito_compras)