# El método popitem() te permite eliminar un par clave-valor de un diccionario de una manera un poco diferente a pop(). Mientras que pop() elimina un elemento específico por su
#  clave, popitem() elimina un elemento arbitrario (generalmente 
# el último insertado en las versiones recientes de Python) y te
#  devuelve tanto la clave como el valor de ese elemento. Piensa
#  en él como si estuvieras sacando el último elemento que metiste
#  en una bolsa, sin preocuparte por su "nombre", y al sacarlo, 
# te das cuenta de qué era y su valor.

# ¿Para qué sirve o qué hace?
# Eliminar y obtener el último elemento (Python 3.7+): En las 
# versiones modernas de Python (3.7 y posteriores), popitem() 
# elimina y devuelve el par clave-valor que fue insertado más 
# recientemente en el diccionario.
# Procesamiento LIFO (Last In, First Out): Esto lo hace útil 
# para implementar una especie de pila o para procesar elementos 
# en el orden inverso al que fueron agregados.
# Vaciar un diccionario: Puedes usarlo repetidamente en un bucle 
# para vaciar un diccionario por completo, procesando cada elemento 
# a medida que lo sacas.
# Gestión de diccionarios con orden garantizado: Es especialmente 
# útil en contextos donde el orden de inserción es importante y 
# quieres procesar los elementos en ese orden inverso.

# Nuestro diccionario de tareas: tarea y su prioridad
tareas_pendientes = {
    "comprar_leche": "alta",
    "enviar_email": "media",
    "llamar_cliente": "urgente",
    "revisar_informe": "baja"
}

print("Tareas pendientes iniciales:", tareas_pendientes)

# --- Usando popitem() para procesar la última tarea ---
print("\n--- Procesando tareas con popitem() ---")

# La "última" tarea añadida es 'revisar_informe'
tarea_clave, tarea_valor = tareas_pendientes.popitem()
print(f"Se procesó la tarea '{tarea_clave}' con prioridad '{tarea_valor}'.")
print("Tareas pendientes restantes:", tareas_pendientes)

# Volvemos a usar popitem()
tarea_clave, tarea_valor = tareas_pendientes.popitem()
print(f"Se procesó la tarea '{tarea_clave}' con prioridad '{tarea_valor}'.")
print("Tareas pendientes restantes:", tareas_pendientes)

# --- Demostración de error si el diccionario está vacío ---
print("\n--- Demostración de KeyError con diccionario vacío ---")
# Vaciar el resto del diccionario para el ejemplo
tareas_pendientes.popitem()
tareas_pendientes.popitem()
print("Diccionario después de vaciar:", tareas_pendientes)

try:
    # Esto causará un KeyError porque el diccionario está vacío
    tareas_pendientes.popitem()
except KeyError:
    print("¡Error! El diccionario está vacío. No se puede usar popitem().")

print("Estado final del diccionario:", tareas_pendientes)