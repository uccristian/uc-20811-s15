# Concatenar listas es unir dos o más listas para crear una NUEVA lista.
# Esto se logra usando el operador de suma (+).
# Es como juntar dos segmentos de una cadena para formar una cadena más larga.
# Las listas originales no se modifican.

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2
print(lista_concatenada) # [1, 2, 3, 4, 5, 6]

nombres1 = ["Ana", "Luis"]
nombres2 = ["Marta", "Pedro"]
todos_los_nombres = nombres1 + nombres2
print(todos_los_nombres) # ['Ana', 'Luis', 'Marta', 'Pedro']