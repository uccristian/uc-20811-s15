# Cada clave en el diccionario ("ana", "luis", etc.) 
# es convertida internamente en un número hash. 
# Esos números son como ubicaciones mágicas que permiten que Python encuentre los datos en microsegundos,
# sin tener que buscar uno por uno.

usuarios = {
    "ana": "administradora",
    "luis": "editor",
    "carla": "visitante"
}

# Ver el hash de cada clave
for nombre in usuarios:
    print(f"Hash de '{nombre}':", hash(nombre))
