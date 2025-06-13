# sort() ordena los elementos de la lista *en su lugar*.
# Esto significa que la lista original se modifica directamente.
# Por defecto, ordena de forma ascendente (de menor a mayor o alfabéticamente).

numeros = [5, 2, 8, 1, 9]
numeros.sort()
print(numeros) # [1, 2, 5, 8, 9]

nombres = ["Carlos", "Ana", "Luis"]
nombres.sort()
print(nombres) # ['Ana', 'Carlos', 'Luis']

precios = [50, 20, 80]
precios.sort(reverse=True)
print(precios) # [80, 50, 20]