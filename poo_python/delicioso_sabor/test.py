from Producto import Producto
from Pedido import Pedido

milanesa = Producto("milanesa", 100, 5)
coca = Producto("coca-cola", 20, 10)
ensalada = Producto("ensalada", 50, 2)

print(f'prueba de pedido sin falla')
mesa1 = Pedido([(1, milanesa), (2, coca), (1, ensalada)])
print(f'Estado: {mesa1.estado}')
mesa1.pedido_para_preparar()
print(mesa1.costo_total(), f"id {mesa1.ver_id()}")
print(f'Estado: {mesa1.estado}')

mesa1.pedido_preparado()
print(f'Estado: {mesa1.estado}')

mesa1.pedido_entregado()
print(f'Estado: {mesa1.estado}')

print(f'prueba de pedido con falta de stock')
mesa2 = Pedido([(2, milanesa), (3, ensalada)])
print(f'Estado: {mesa2.estado}')
mesa2.pedido_para_preparar()
# falta agregar descontar el pedido del stock

print(mesa2.costo_total(), f"id {mesa2.ver_id()}")
print(f'Estado: {mesa2.estado}')