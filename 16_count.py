# count() te dice CUÁNTAS VECES aparece un elemento específico en la lista.
# Es como si contaras cuántos caramelos rojos hay en una bolsa llena de caramelos de colores.

# Lista de números con repeticiones
numeros_juego = [1, 2, 2, 3, 1, 4, 2]
apariciones_dos = numeros_juego.count(2)
print(apariciones_dos) # 3

# Contar cuántas veces aparece un número que no está en la lista
apariciones_cinco = numeros_juego.count(5)
print(apariciones_cinco) # 0

# Otro ejemplo con una lista de palabras
lista_frutas = ["manzana", "banana", "manzana", "cereza", "manzana"]
conteo_manzanas = lista_frutas.count("manzana")
print(conteo_manzanas) # 3