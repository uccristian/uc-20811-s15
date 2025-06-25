usuarios = {
    "ana": "administradora",
    "luis": "editor",
    "carla": "visitante"
}

for nombre in usuarios:
    print(f"Hash de '{nombre}':", hash(nombre))


