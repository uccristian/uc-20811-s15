# sorted() es una función que te da una NUEVA lista con los elementos ordenados.
# ¡Importante! La lista original NO se modifica.
# Es como si le dieras un mazo de cartas desordenado a alguien, y esa persona te devuelve
# un mazo NUEVO ya ordenado, mientras tu mazo original sigue desordenado en tu mano.

temperaturas = [25, 18, 30, 22, 19]
temperaturas_ordenadas = sorted(temperaturas)
print(temperaturas_ordenadas) # [18, 19, 22, 25, 30]
print(temperaturas) # [25, 18, 30, 22, 19]

palabras = ["gato", "perro", "ave", "pez"]
palabras_alfabeticas = sorted(palabras)
print(palabras_alfabeticas) # ['ave', 'gato', 'pez', 'perro']
print(palabras) # ['gato', 'perro', 'ave', 'pez']

puntuaciones = [85, 92, 78]
puntuaciones_desc = sorted(puntuaciones, reverse=True)
print(puntuaciones_desc) # [92, 85, 78]