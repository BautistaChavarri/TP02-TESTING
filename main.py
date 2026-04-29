from app.descuentos import calcular_precio_final

precio = 1000
descuento = 20

resultado = calcular_precio_final(precio, descuento)

print(f"Precio original: ${precio}")
print(f"Descuento aplicado: {descuento}%")
print(f"Precio final: ${resultado}")