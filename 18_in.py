# El operador 'in' se usa para verificar si un elemento EXISTE dentro de una lista.
# Devuelve True (verdadero) si el elemento está en la lista, y False (falso) si no lo está.
# Es como preguntar: "¿Está este libro en esta estantería?" La respuesta es sí o no.

productos_stock = ["leche", "pan", "huevos", "queso"]
hay_pan = "pan" in productos_stock
print(hay_pan) # True

numeros_primos = [2, 3, 5, 7, 11]
es_cinco_primo = 5 in numeros_primos
print(es_cinco_primo) # True
es_cuatro_primo = 4 in numeros_primos
print(es_cuatro_primo) # False