# tuple() es una función que se usa para CREAR una tupla a partir de otros elementos,
# especialmente de una lista o cualquier otra "cosa" que pueda ser iterada (como una cadena de texto).
# Es útil cuando ya tienes datos en otro formato y quieres convertirlos a una tupla
# porque necesitas la inmutabilidad de una tupla (que no cambien los datos).

lista_de_numeros = [1, 2, 3, 4]
mi_tupla = tuple(lista_de_numeros)
print(mi_tupla) # (1, 2, 3, 4)

# La lista original no se modifica
print(lista_de_numeros) # [1, 2, 3, 4]

# Ejemplo 2: Crear una tupla a partir de una cadena de texto
# Cada carácter se convierte en un elemento de la tupla
nombre = "Python"
tupla_letras = tuple(nombre)
print(tupla_letras) # ('P', 'y', 't', 'h', 'o', 'n')

# Ejemplo 4: Crear una tupla con un solo elemento (¡nota la coma!)
# Si no pones la coma, Python lo trata como un simple valor entre paréntesis.
tupla_un_elemento = (5,) # La coma es crucial aquí
print(tupla_un_elemento) # (5,)
