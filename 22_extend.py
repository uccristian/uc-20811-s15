mi_tupla_inicial = (1, 2)
mi_lista_para_modificar = list(mi_tupla_inicial)
print(mi_lista_para_modificar)

elementos_extras = [3, 4, 5]
mi_lista_para_modificar.extend(elementos_extras)
print(mi_lista_para_modificar) 

nueva_tupla_extendida = tuple(mi_lista_para_modificar)
print(nueva_tupla_extendida) 

print(mi_tupla_inicial)
