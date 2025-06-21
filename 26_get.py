info_libro = {
    "titulo": "El Principito",
    "autor": "Antoine de Saint-Exupéry",
    "año_publicacion": 1943
}

titulo = info_libro.get("titulo")
print(titulo)
idioma = info_libro.get("idioma")
print(idioma)
genero = info_libro.get("genero", "Desconocido")
print(genero)

