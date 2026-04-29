def calcular_precio_final(precio, descuento):
    if precio <= 0:
        raise ValueError("El precio debe ser mayor a 0")

    if descuento < 0 or descuento > 100:
        raise ValueError("El descuento debe estar entre 0 y 100")

    precio_final = precio - (precio * descuento / 100)
    return precio_final