carrito_compras = {
    "manzanas": 5,
    "leche": 2,
    "pan": 1,
    "huevos": 12
}

cantidad_manzanas = carrito_compras.pop("manzanas")
print(carrito_compras)
cantidad_galletas = carrito_compras.pop("galletas", 0)
print(carrito_compras)
