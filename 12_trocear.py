# Trocear (o "slicing") es una forma de obtener una PARTE (un "trozo" o sub-lista) de una lista.
# Es como cortar un pedazo de un pastel sin afectar el resto del pastel.
# Se usa la notación de corchetes [] con índices: [inicio:fin:paso].
# El 'inicio' es donde empieza el trozo (incluido).
# El 'fin' es donde termina el trozo (NO incluido).
# El 'paso' es de cuánto en cuánto "saltar" (por defecto es 1).
# Siempre crea una NUEVA lista.

dias_semana = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]
# Ejemplo 1: Obtener los primeros 3 días (del índice 0 al 3, sin incluir el 3)
primeros_dias = dias_semana[0:3]
print(primeros_dias) # ['Lun', 'Mar', 'Mie']

# Ejemplo 2: Obtener los días de fin de semana (del índice 5 al final)
fin_semana = dias_semana[5:]
print(fin_semana) # ['Sab', 'Dom']

# Ejemplo 3: Obtener desde el principio hasta un índice específico (hasta el 4, sin incluir el 4)
hasta_jueves = dias_semana[:4]
print(hasta_jueves) # ['Lun', 'Mar', 'Mie', 'Jue']

# Ejemplo 4: Obtener todos los elementos (una copia de la lista)
copia_dias = dias_semana[:]
print(copia_dias) # ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

# Ejemplo 5: Trocear con 'paso' (cada dos elementos)
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = numeros[0:10:2] # Del principio al final, saltando de 2 en 2
print(pares) # [0, 2, 4, 6, 8]
