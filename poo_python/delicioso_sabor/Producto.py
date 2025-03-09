class Producto:
    
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def ingresar_stock(self, valor):
        self.cantidad += valor
    
    def retirar_stock(self, valor):
        if self.suficiente_stock(valor):
            self.cantidad -= valor
        else:
            print("No hay stock suficiente")
    
    def suficiente_stock(self, valor):
        return self.cantidad >= valor 