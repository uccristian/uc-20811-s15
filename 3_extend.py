# extend() agrega todos los elementos de otra lista (o similar) al final de la lista actual.

frutas = ["manzana", "banana"]
frutas_tropicales = ["mango", "piña"]

frutas.extend(frutas_tropicales)
print(frutas) # ['manzana', 'banana', 'mango', 'piña']

lista_a = [1, 2]
lista_b = [3, 4]

lista_a.extend(lista_b)
print(lista_a) # [1, 2, 3, 4]