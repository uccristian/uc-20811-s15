# Replicar listas es como "repetir" una lista un número específico de veces
# para crear una NUEVA lista más grande.
# Se usa el operador de multiplicación (*).
# Es como fotocopiar una lista varias veces y luego unirlas.
# La lista original no se modifica.

lista_base = ["a", "b"]
lista_replicada = lista_base * 3
print(lista_replicada) # ['a', 'b', 'a', 'b', 'a', 'b']
print(lista_base) # ['a', 'b']

numeros_simples = [0, 1]
numeros_multiplicados = numeros_simples * 4
print(numeros_multiplicados) # [0, 1, 0, 1, 0, 1, 0, 1]