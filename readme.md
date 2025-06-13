# Presentación de Operaciones con Listas y Tuplas en Python

Este repositorio contiene el material de una presentación detallada sobre las operaciones fundamentales con **Listas** y **Tuplas** en Python. El objetivo es proporcionar una comprensión clara y con ejemplos sencillos de cómo manipular y trabajar con estas estructuras de datos esenciales.

### Contenido de la Presentación

La presentación cubre los siguientes puntos, organizados para facilitar el aprendizaje y la comprensión:

#### Operaciones con Listas (`list`)

* **List**: Descripción general de qué son las listas y cómo se declaran.
* **`append()`**: Cómo añadir un elemento al final de una lista.
* **`extend()`**: Cómo añadir múltiples elementos de otra secuencia al final de una lista.
* **`insert()`**: Cómo insertar un elemento en una posición específica de la lista.
* **`del`**: Cómo eliminar elementos por su índice o rango, o la lista completa.
* **`remove()`**: Cómo eliminar la primera aparición de un elemento por su valor.
* **`reversed()`**: Cómo obtener un iterador de los elementos en orden inverso (sin modificar la lista original).
* **`sort()`**: Cómo ordenar la lista en su lugar (modifica la lista original).
* **`sorted()`**: Cómo obtener una *nueva* lista ordenada (la original no cambia).
* **Concatenar**: Unir dos o más listas usando el operador `+`.
* **Replicar**: Repetir una lista un número de veces usando el operador `*`.
* **Trocear (Slicing)**: Extraer sub-listas utilizando rangos de índices `[inicio:fin:paso]`.
* **`min()`**: Encontrar el elemento más pequeño de una lista.
* **`max()`**: Encontrar el elemento más grande de una lista.
* **`index()`**: Obtener la posición (índice) de la primera aparición de un elemento.
* **`count()`**: Contar cuántas veces aparece un elemento en la lista.
* **`sum()`**: Sumar todos los elementos numéricos de una lista.
* **`in`**: Verificar si un elemento está presente en la lista.

#### Operaciones con Tuplas (`tuple`)

* **Tupla (`tuple`)**: Descripción de qué son las tuplas y cómo se diferencian de las listas (su inmutabilidad).
* **`tuple()` (función)**: Cómo convertir otras secuencias (como listas o cadenas) en tuplas.
* **`append()` (en tuplas)**: Explicación de por qué no existe y cómo se "simula" mediante la creación de una nueva tupla.
* **`reverse()` (en tuplas)**: Explicación de por qué no existe y cómo se "simula" obteniendo una nueva tupla invertida.
* **`extend()` (en tuplas)**: Explicación de por qué no existe y cómo se "simula" mediante la creación de una nueva tupla concatenada.
* **`remove()` (en tuplas)**: Explicación de por qué no existe y cómo se "simula" creando una nueva tupla sin el elemento.
* **`clear()` (en tuplas)**: Explicación de por qué no existe y cómo se "simula" reasignando una tupla vacía.

### Cómo Usar este Recurso

Los ejemplos de código se proporcionan de manera clara y concisa, incluyendo las salidas esperadas en los comentarios para una fácil comprensión. Puedes copiar y pegar los fragmentos de código en tu propio entorno Python para experimentar con ellos.

Para ejecutar los ejemplos:
1.  Asegúrate de tener **Python 3** instalado en tu sistema.
2.  Copia los fragmentos de código del tema que te interese en un archivo `.py` (por ejemplo, `ejemplos.py`).
3.  Ejecuta el archivo desde tu terminal: `python ejemplos.py`