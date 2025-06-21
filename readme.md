# Propiedades y Métodos Clave en Python

Este informe detalla las propiedades fundamentales y métodos comunes de las estructuras de datos más importantes en Python: **Listas**, **Tuplas**, **Diccionarios** y **Conjuntos**. Para cada elemento, se explica su función principal y se proporciona un ejemplo de código sencillo.

---

## Listas (`list`)

Las **listas** son colecciones ordenadas y **mutables** (modificables) de elementos. Puedes guardar cualquier tipo de dato en una lista, y sus elementos son accesibles por un índice numérico.

### `list` (Tipo de dato)
Una **lista** es una secuencia de elementos que puedes modificar. Es como una caja con compartimentos numerados donde puedes guardar cosas en cualquier orden, añadir más, quitar algunas o cambiar lo que hay dentro.

```python
# Ejemplo de creación de una lista
frutas = ["manzana", "platano", "cereza"]
print(f"Lista de frutas: {frutas}")
```

### `append()`
El método `append()` **añade un único elemento al final** de la lista.

```python
frutas = ["manzana", "platano"]
frutas.append("naranja")
print(f"Después de append(): {frutas}") # Salida: ['manzana', 'platano', 'naranja']
```

### `extend()`
El método `extend()` **añade todos los elementos de un iterable** (como otra lista) al final de la lista actual.

```python
numeros = [1, 2, 3]
mas_numeros = [4, 5]
numeros.extend(mas_numeros)
print(f"Después de extend(): {numeros}") # Salida: [1, 2, 3, 4, 5]
```

### `insert()`
El método `insert()` **añade un elemento en una posición específica** (índice) dentro de la lista.

```python
letras = ["a", "c", "d"]
letras.insert(1, "b") # Inserta 'b' en el índice 1
print(f"Después de insert(): {letras}") # Salida: ['a', 'b', 'c', 'd']
```

### `del` (Palabra clave)
La palabra clave `del` **elimina un elemento de la lista por su índice** o una porción de la lista (trozo).

```python
colores = ["rojo", "verde", "azul", "amarillo"]
del colores[1] # Elimina el elemento en el índice 1 ('verde')
print(f"Después de del por índice: {colores}") # Salida: ['rojo', 'azul', 'amarillo']

# También se puede usar para eliminar un rango
del colores[1:3] # Elimina desde el índice 1 hasta el 2
print(f"Después de del por rango: {colores}") # Salida: ['rojo']
```

### `remove()`
El método `remove()` **elimina la primera ocurrencia de un valor específico** de la lista.

```python
animales = ["perro", "gato", "perro", "pez"]
animales.remove("perro")
print(f"Después de remove(): {animales}") # Salida: ['gato', 'perro', 'pez']
```

### `reversed()`
La función `reversed()` **devuelve un iterador que produce los elementos de la lista en orden inverso**. No modifica la lista original.

```python
valores = [10, 20, 30, 40]
valores_invertidos = list(reversed(valores)) # Convertir el iterador a lista
print(f"Lista original: {valores}")
print(f"Lista invertida (usando reversed()): {valores_invertidos}") # Salida: [40, 30, 20, 10]
```

### `sort()`
El método `sort()` **ordena la lista en su lugar** (modifica la lista original). Por defecto, ordena de forma ascendente.

```python
numeros_desordenados = [3, 1, 4, 1, 5, 9, 2]
numeros_desordenados.sort()
print(f"Después de sort(): {numeros_desordenados}") # Salida: [1, 1, 2, 3, 4, 5, 9]

# Orden descendente
numeros_desordenados.sort(reverse=True)
print(f"Después de sort(reverse=True): {numeros_desordenados}")
```

### `sorted()`
La función `sorted()` **devuelve una nueva lista ordenada** a partir de los elementos de un iterable. No modifica el iterable original.

```python
puntuaciones = [85, 92, 78, 95, 88]
puntuaciones_ordenadas = sorted(puntuaciones)
print(f"Puntuaciones originales: {puntuaciones}")
print(f"Puntuaciones ordenadas (usando sorted()): {puntuaciones_ordenadas}") # Salida: [78, 85, 88, 92, 95]
```

### Concatenar (`+`)
La operación de concatenación `+` **une dos o más listas** para crear una nueva lista.

```python
lista1 = [1, 2]
lista2 = [3, 4]
lista_concatenada = lista1 + lista2
print(f"Listas concatenadas: {lista_concatenada}") # Salida: [1, 2, 3, 4]
```

### Replicar (`*`)
La operación de replicación `*` **crea una nueva lista repitiendo los elementos** de la lista original un número específico de veces.

```python
elemento = ["a"]
lista_replicada = elemento * 3
print(f"Lista replicada: {lista_replicada}") # Salida: ['a', 'a', 'a']
```

### Trocear (`[]` con `:`)
El troceado (slicing) permite **extraer una porción (sub-lista)** de una lista utilizando índices de inicio y fin.

```python
numeros_grandes = [10, 20, 30, 40, 50, 60]
sub_lista = numeros_grandes[1:4] # Elementos desde el índice 1 (incluido) hasta el 4 (excluido)
print(f"Sub-lista troceada: {sub_lista}") # Salida: [20, 30, 40]
```

### `min()`
La función `min()` **devuelve el elemento más pequeño** de la lista.

```python
precios = [25.5, 12.0, 30.75, 18.2]
precio_minimo = min(precios)
print(f"Precio mínimo: {precio_minimo}") # Salida: 12.0
```

### `max()`
La función `max()` **devuelve el elemento más grande** de la lista.

```python
temperaturas = [20, 25, 18, 30, 22]
temperatura_maxima = max(temperaturas)
print(f"Temperatura máxima: {temperatura_maxima}") # Salida: 30
```

### `index()`
El método `index()` **devuelve el índice de la primera ocurrencia** de un valor específico en la lista. Si el valor no se encuentra, genera un `ValueError`.

```python
colores = ["rojo", "verde", "azul", "verde"]
indice_verde = colores.index("verde")
print(f"El primer 'verde' está en el índice: {indice_verde}") # Salida: 1
```

### `count()`
El método `count()` **devuelve el número de veces que un valor específico aparece** en la lista.

```python
letras_repetidas = ["a", "b", "a", "c", "a"]
conteo_a = letras_repetidas.count("a")
print(f"La letra 'a' aparece {conteo_a} veces.") # Salida: 3
```

### `sum()`
La función `sum()` **devuelve la suma de todos los elementos numéricos** de la lista.

```python
gastos = [50, 15.5, 20.0, 10.25]
total_gastos = sum(gastos)
print(f"Total de gastos: {total_gastos}") # Salida: 95.75
```

### `in` (Operador de pertenencia)
El operador `in` **verifica si un elemento existe** en la lista. Devuelve `True` si el elemento está, y `False` si no.

```python
participantes = ["Juan", "Maria", "Pedro"]
esta_juan = "Juan" in participantes
esta_luisa = "Luisa" in participantes
print(f"¿Está Juan en la lista? {esta_juan}")   # Salida: True
print(f"¿Está Luisa en la lista? {esta_luisa}") # Salida: False
```

---

## Tuplas (`tuple`)

Las **tuplas** son colecciones ordenadas e **inmutables**. Una vez que creas una tupla, no puedes cambiar, añadir o eliminar sus elementos.

### `tuple` (Tipo de dato)
Una **tupla** es una secuencia de elementos ordenada e **inmutable**. Es como una lista, pero una vez que metes los elementos, no puedes cambiarlos. Son útiles para datos que no deben modificarse, como coordenadas geográficas o una fecha.

```python
# Ejemplo de creación de una tupla
coordenadas = (10.5, 20.3)
colores_rgb = (255, 0, 0) # Rojo
print(f"Coordenadas: {coordenadas}")
print(f"Color RGB: {colores_rgb}")
```

### `append()` (Estrategia para inmutabilidad)
Dado que las tuplas son inmutables, no tienen un método `append()`. Para "añadir" un elemento, se convierte la tupla a una lista, se añade el elemento, y luego se vuelve a convertir en tupla.

```python
mi_tupla = (1, 2)
print(f"Tupla original: {mi_tupla}")

# Convertir a lista, añadir y convertir de nuevo a tupla
lista_temporal = list(mi_tupla)
lista_temporal.append(3)
nueva_tupla = tuple(lista_temporal)
print(f"Tupla después de 'append' (simulado): {nueva_tupla}") # Salida: (1, 2, 3)
```

### `reverse()` (Estrategia para inmutabilidad)
Las tuplas no tienen un método `reverse()` porque son inmutables. Para invertir el orden, se convierte la tupla a una lista, se invierte la lista, y luego se vuelve a convertir en tupla. Alternativamente, se puede usar `reversed()`.

```python
numeros_tupla = (1, 2, 3, 4)
print(f"Tupla original: {numeros_tupla}")

# Opción 1: Convertir a lista, invertir, y volver a tupla
lista_temp = list(numeros_tupla)
lista_temp.reverse()
tupla_invertida = tuple(lista_temp)
print(f"Tupla invertida (simulando reverse): {tupla_invertida}") # Salida: (4, 3, 2, 1)

# Opción 2: Usar la función reversed()
tupla_invertida_2 = tuple(reversed(numeros_tupla))
print(f"Tupla invertida (usando reversed()): {tupla_invertida_2}") # Salida: (4, 3, 2, 1)
```

### `extend()` (Estrategia para inmutabilidad)
Al igual que `append()`, las tuplas no tienen `extend()`. Para "extender" una tupla, se convierte a lista, se extiende la lista, y luego se convierte de nuevo en tupla. También se puede usar la concatenación de tuplas.

```python
tupla_a = (1, 2)
tupla_b = (3, 4)
print(f"Tupla A: {tupla_a}, Tupla B: {tupla_b}")

# Opción 1: Convertir a lista, extender, y volver a tupla
lista_temp = list(tupla_a)
lista_temp.extend(tupla_b)
tupla_extendida = tuple(lista_temp)
print(f"Tupla extendida (simulando extend): {tupla_extendida}") # Salida: (1, 2, 3, 4)

# Opción 2: Usar concatenación de tuplas (más común para tuplas)
tupla_extendida_2 = tupla_a + tupla_b
print(f"Tupla extendida (usando concatenación): {tupla_extendida_2}") # Salida: (1, 2, 3, 4)
```

### `remove()` (Estrategia para inmutabilidad)
Las tuplas no tienen un método `remove()`. Para "remover" un elemento por valor, se convierte la tupla a lista, se usa `remove()` en la lista, y se vuelve a convertir a tupla.

```python
colores_tupla = ("rojo", "verde", "azul")
print(f"Tupla original: {colores_tupla}")

# Convertir a lista, remover, y volver a tupla
lista_temp = list(colores_tupla)
if "verde" in lista_temp: # Es buena práctica verificar antes de remover
    lista_temp.remove("verde")
nueva_colores_tupla = tuple(lista_temp)
print(f"Tupla después de 'remove' (simulado): {nueva_colores_tupla}") # Salida: ('rojo', 'azul')
```

### `clear()` (Estrategia para inmutabilidad)
Las tuplas no tienen un método `clear()`. Para "vaciar" una tupla, la forma más sencilla es reasignar la variable a una tupla vacía ().

```python
elementos_tupla = (10, 20, 30)
print(f"Tupla original: {elementos_tupla}")

# Reasignar la tupla a una tupla vacía para 'vaciarla'
elementos_tupla = ()
print(f"Tupla después de 'clear' (simulado): {elementos_tupla}") # Salida: ()
```

---

## Diccionarios (`dict`)

Los **diccionarios** son colecciones no ordenadas (en versiones antiguas, ordenadas por inserción a partir de Python 3.7) de pares **clave-valor**. Cada clave debe ser única y se usa para acceder a su valor asociado.

### `dict` (Tipo de dato)
Un **diccionario** es una colección de pares donde cada pieza de información se guarda con una **clave** única que la identifica. Es como un diccionario de la vida real donde una palabra (clave) tiene una definición (valor) asociada.

```python
# Ejemplo de creación de un diccionario
persona = {
    "nombre": "Elena",
    "edad": 28,
    "ciudad": "Madrid"
}
print(f"Diccionario persona: {persona}")
```

### `get()`
El método `get()` **devuelve el valor para la clave especificada**. Si la clave no existe, devuelve `None` o un valor por defecto si se especifica.

```python
configuracion = {"tema": "oscuro", "idioma": "es"}
tema_actual = configuracion.get("tema")
print(f"Tema actual: {tema_actual}") # Salida: oscuro

# Clave no existente, con valor por defecto
fuente = configuracion.get("fuente", "Arial")
print(f"Fuente (por defecto): {fuente}") # Salida: Arial
```

### `keys()`
El método `keys()` **devuelve una vista de todas las claves** del diccionario. Esta vista se actualiza si el diccionario cambia.

```python
productos = {"manzana": 1.2, "platano": 0.8, "cereza": 3.5}
nombres_productos = productos.keys()
print(f"Claves de productos: {nombres_productos}") # Salida: dict_keys(['manzana', 'platano', 'cereza'])

# Puedes iterar sobre ellas
print("Productos disponibles:")
for p in nombres_productos:
    print(f"- {p}")
```

### `values()`
El método `values()` **devuelve una vista de todos los valores** del diccionario. Esta vista se actualiza si el diccionario cambia.

```python
temperaturas_ciudades = {"Madrid": 25, "Paris": 22, "Roma": 28}
solo_temperaturas = temperaturas_ciudades.values()
print(f"Valores de temperaturas: {solo_temperaturas}") # Salida: dict_values([25, 22, 28])

# Puedes iterar sobre ellos
print("Temperaturas reportadas:")
for temp in solo_temperaturas:
    print(f"{temp}°C")
```

### `items()`
El método `items()` **devuelve una vista de todos los pares clave-valor** del diccionario como tuplas. Esta vista se actualiza si el diccionario cambia.

```python
puntuaciones_alumnos = {"Ana": 90, "Luis": 85, "Marta": 92}
pares_alumno_puntuacion = puntuaciones_alumnos.items()
print(f"Items de puntuaciones: {pares_alumno_puntuacion}") # Salida: dict_items([('Ana', 90), ('Luis', 85), ('Marta', 92)])

# Puedes iterar desempaquetando clave y valor
print("Puntuaciones de cada alumno:")
for alumno, puntuacion in pares_alumno_puntuacion:
    print(f"{alumno}: {puntuacion}")
```

### `pop()`
El método `pop()` **elimina el elemento con la clave especificada y devuelve su valor**. Si la clave no existe y no se proporciona un valor por defecto, genera un `KeyError`.

```python
inventario = {"lapices": 100, "boligrafos": 50, "papel": 200}
cantidad_lapices = inventario.pop("lapices")
print(f"Se retiraron {cantidad_lapices} lápices.")
print(f"Inventario restante: {inventario}") # Salida: {'boligrafos': 50, 'papel': 200}

# Intentar eliminar una clave inexistente con valor por defecto
cantidad_gomas = inventario.pop("gomas", 0)
print(f"Se intentaron retirar gomas: {cantidad_gomas}") # Salida: 0
print(f"Inventario (sin cambios): {inventario}")
```

### `popitem()`
El método `popitem()` **elimina y devuelve un par clave-valor** (como tupla) del diccionario. En Python 3.7+, elimina el último par insertado. Si el diccionario está vacío, genera un `KeyError`.

```python
tareas = {"tarea1": "pendiente", "tarea2": "en progreso", "tarea3": "completada"}
print(f"Tareas iniciales: {tareas}")

ultima_tarea_clave, ultima_tarea_estado = tareas.popitem()
print(f"Se completó la última tarea: '_{ultima_tarea_clave}_' con estado '_{ultima_tarea_estado}_'.")
print(f"Tareas restantes: {tareas}") # Salida: {'tarea1': 'pendiente', 'tarea2': 'en progreso'}
```

### `del` (Palabra clave)
La palabra clave `del` **elimina un par clave-valor específico** del diccionario por su clave. Si la clave no existe, genera un `KeyError`.

```python
contactos = {"Juan": "123-456", "Maria": "789-012", "Pedro": "345-678"}
print(f"Contactos iniciales: {contactos}")

del contactos["Maria"]
print(f"Después de eliminar a Maria: {contactos}") # Salida: {'Juan': '123-456', 'Pedro': '345-678'}

# Ejemplo de error si la clave no existe
try:
    del contactos["Luis"]
except KeyError:
    print("¡Error! Luis no estaba en los contactos.")
```

### `clear()`
El método `clear()` **elimina todos los pares clave-valor** del diccionario, dejándolo vacío.

```python
datos_sesion = {"usuario": "admin", "token": "abc123xyz", "expira": "2025-01-01"}
print(f"Datos de sesión iniciales: {datos_sesion}")

datos_sesion.clear()
print(f"Después de clear(): {datos_sesion}") # Salida: {}
```

### `hash()`
La función `hash()` **devuelve el valor hash de un objeto**. Las claves de un diccionario deben ser **hasheables** (es decir, inmutables y tener un valor hash constante). Esto significa que no puedes usar listas o diccionarios como claves directamente porque son mutables y, por lo tanto, no hasheables.

```python
# Ejemplo de objetos hasheables (pueden ser claves de diccionario)
print(f"Hash de 'hola': {hash('hola')}")
print(f"Hash de 123: {hash(123)}")
print(f"Hash de (1, 2): {hash((1, 2))}") # Las tuplas son hasheables

# Intentar hashear un objeto no hasheable (listas, diccionarios) resultará en TypeError
try:
    hash([1, 2])
except TypeError as e:
    print(f"Error al hashear una lista: {e}") # Salida: TypeError: unhashable type: 'list'
```

---

## Conjuntos (`set`)

Los **conjuntos** son colecciones **no ordenadas** de elementos **únicos**. Esto significa que un conjunto no puede tener elementos duplicados. Son útiles para operaciones matemáticas de conjuntos como unión, intersección, etc.

### `set` (Tipo de dato)
Un **conjunto** es una colección de elementos donde cada elemento es único y no tiene un orden definido. Es como una bolsa de canicas de diferentes colores, pero si intentas meter dos canicas del mismo color, solo se cuenta una.

```python
# Ejemplo de creación de un conjunto
# Los duplicados se eliminan automáticamente
numeros_unicos = {1, 2, 3, 2, 4}
print(f"Conjunto de números: {numeros_unicos}") # Salida: {1, 2, 3, 4}

# Crear un conjunto a partir de una lista
letras = set(["a", "b", "a", "c"])
print(f"Conjunto de letras: {letras}") # Salida: {'a', 'b', 'c'}
```

### `add()`
El método `add()` **añade un elemento único al conjunto**. Si el elemento ya existe, el conjunto no cambia.

```python
frutas_favoritas = {"manzana", "platano"}
frutas_favoritas.add("naranja")
print(f"Después de add('naranja'): {frutas_favoritas}") # Salida: {'manzana', 'platano', 'naranja'}

frutas_favoritas.add("manzana") # No hace nada, ya existe
print(f"Después de add('manzana') de nuevo: {frutas_favoritas}")
```

### `remove()`
El método `remove()` **elimina un elemento específico del conjunto**. Si el elemento no existe, genera un `KeyError` (similar al diccionario).

```python
participantes_set = {"Ana", "Luis", "Marta"}
participantes_set.remove("Luis")
print(f"Después de remove('Luis'): {participantes_set}") # Salida: {'Ana', 'Marta'}

try:
    participantes_set.remove("Pedro")
except KeyError:
    print("¡Error! Pedro no estaba en el conjunto.")
```

### `discard()`
El método `discard()` **elimina un elemento específico del conjunto si existe**. A diferencia de `remove()`, **no genera un error** si el elemento no se encuentra.

```python
colores_set = {"rojo", "verde", "azul"}
colores_set.discard("verde")
print(f"Después de discard('verde'): {colores_set}") # Salida: {'rojo', 'azul'}

colores_set.discard("amarillo") # No hace nada y no da error
print(f"Después de discard('amarillo'): {colores_set}") # Salida: {'rojo', 'azul'}
```

### `sorted()`
La función `sorted()` **devuelve una nueva lista con los elementos del conjunto ordenados**. Los conjuntos en sí no tienen un orden, pero esta función permite ver sus elementos de forma ordenada.

```python
edades = {25, 30, 22, 28}
edades_ordenadas = sorted(edades)
print(f"Conjunto original: {edades}")
print(f"Edades ordenadas (usando sorted()): {edades_ordenadas}") # Salida: [22, 25, 28, 30]
```

### Intersección (`intersection()` o `&`)
La intersección **devuelve un nuevo conjunto con los elementos que son comunes** a ambos conjuntos.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Usando el método intersection()
interseccion_metodo = set1.intersection(set2)
print(f"Intersección (método): {interseccion_metodo}") # Salida: {3, 4}

# Usando el operador &
interseccion_operador = set1 & set2
print(f"Intersección (operador): {interseccion_operador}") # Salida: {3, 4}
```

### Unión (`union()` o `|`)
La unión **devuelve un nuevo conjunto con todos los elementos de ambos conjuntos**, sin duplicados.

```python
set_a = {"manzana", "platano"}
set_b = {"platano", "naranja", "uva"}

# Usando el método union()
union_metodo = set_a.union(set_b)
print(f"Unión (método): {union_metodo}") # Salida: {'manzana', 'platano', 'naranja', 'uva'} (el orden puede variar)

# Usando el operador |
union_operador = set_a | set_b
print(f"Unión (operador): {union_operador}") # Salida: {'manzana', 'platano', 'naranja', 'uva'}
```

### Diferencia (`difference()` o `-`)
La diferencia **devuelve un nuevo conjunto con los elementos que están en el primer conjunto pero no en el segundo**.

```python
alumnos_clase1 = {"Juan", "Maria", "Pedro", "Ana"}
alumnos_clase2 = {"Maria", "Ana", "Luis"}

# Usando el método difference()
solo_en_clase1 = alumnos_clase1.difference(alumnos_clase2)
print(f"Solo en Clase 1: {solo_en_clase1}") # Salida: {'Juan', 'Pedro'}

# Usando el operador -
solo_en_clase1_op = alumnos_clase1 - alumnos_clase2
print(f"Solo en Clase 1 (operador): {solo_en_clase1_op}") # Salida: {'Juan', 'Pedro'}
```

### Diferencia Simétrica (`symmetric_difference()` o `^`)
La diferencia simétrica **devuelve un nuevo conjunto con los elementos que están en uno de los conjuntos, pero no en ambos** (es decir, todos los elementos que no son comunes).

```python
set_par = {2, 4, 6, 8}
set_impar = {1, 3, 5, 7, 8} # El 8 es para mostrar la diferencia

# Usando el método symmetric_difference()
dif_sim_metodo = set_par.symmetric_difference(set_impar)
print(f"Diferencia simétrica (método): {dif_sim_metodo}") # Salida: {1, 2, 3, 4, 5, 6, 7}

# Usando el operador ^
dif_sim_operador = set_par ^ set_impar
print(f"Diferencia simétrica (operador): {dif_sim_operador}") # Salida: {1, 2, 3, 4, 5, 6, 7}
```

### Inclusión (Subset y Superset)
Se refiere a comprobar si un conjunto es un **subconjunto** de otro (todos sus elementos están en el otro conjunto) o si es un **superconjunto** (contiene todos los elementos del otro conjunto).

* `issubset()` (`<` o `<=`) verifica si el primer conjunto es un subconjunto del segundo.
* `issuperset()` (`>` o `>=`) verifica si el primer conjunto es un superconjunto del segundo.

```python
conjunto_pequeno = {1, 2}
conjunto_grande = {1, 2, 3, 4}

es_subconjunto = conjunto_pequeno.issubset(conjunto_grande)
print(f"¿{conjunto_pequeno} es subconjunto de {conjunto_grande}? {es_subconjunto}") # Salida: True

es_superconjunto = conjunto_grande.issuperset(conjunto_pequeno)
print(f"¿{conjunto_grande} es superconjunto de {conjunto_pequeno}? {es_superconjunto}") # Salida: True

# Con operadores
print(f"¿{conjunto_pequeno} <= {conjunto_grande}? {conjunto_pequeno <= conjunto_grande}") # Salida: True
print(f"¿{conjunto_grande} >= {conjunto_pequeno}? {conjunto_grande >= conjunto_pequeno}") # Salida: True
```

### `frozenset`
Un `frozenset` es una versión **inmutable** de un conjunto. Una vez creado, no puedes añadir, eliminar o modificar sus elementos. Su principal uso es que, al ser inmutable, puede ser utilizado como **clave en un diccionario** o como **elemento dentro de otro conjunto**, algo que los conjuntos normales (mutables) no pueden hacer.

```python
# Crear un frozenset
conjunto_inmutable = frozenset([1, 2, 3])
print(f"Frozenset: {conjunto_inmutable}")

# Intentar añadir un elemento (generará un error)
try:
    conjunto_inmutable.add(4)
except AttributeError as e:
    print(f"Error al intentar añadir a un frozenset: {e}") # Salida: AttributeError: 'frozenset' object has no attribute 'add'

# Usar un frozenset como clave de diccionario
diccionario_con_frozenset_clave = {
    frozenset({"rojo", "verde"}): "Colores primarios"
}
print(f"Diccionario con frozenset como clave: {diccionario_con_frozenset_clave}")
```