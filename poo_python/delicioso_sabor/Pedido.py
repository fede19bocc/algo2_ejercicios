from Producto import Producto

class Pedido:
    id_unico = 1
    
    def __init__(self, items):
        """
        items: Lista de tuplas (cantidad, producto)
        """
        self.items = items 
        self.estado = "ingresado"
        self.id_pedido = Pedido.id_unico   
        Pedido.id_unico += 1
        
    def costo_total(self):
        costo_total = 0
        for cantidad, producto in self.items:
            costo_total += cantidad * producto.precio
        return costo_total * 0.9
    
    # def chequear_pedido(self):
    #     for cantidad, producto in self.items:
    #         if not producto.suficiente_stock(cantidad):
    #             return False
    #     return True
    
    def chequear_pedido(self):
        for cantidad, producto in self.items:  #"producto" en minúscula
            print(f"Verificando stock para {producto.nombre}: {producto.cantidad} disponible, {cantidad} requerido")
            if not producto.suficiente_stock(cantidad):  #Llamamos a `suficiente_stock` del producto
                print(f"FALTA STOCK para {producto.nombre}")
                return False
        return True
    
    def pedido_para_preparar(self):
        if not self.chequear_pedido():  # ✅ Ahora `chequear_pedido()` es seguro
            print("No hay suficiente stock, cambiando estado a 'cambiar'")
            self.estado = "cambiar"
            return

        self.estado = "preparar"
        for cantidad, producto in self.items:
            producto.retirar_stock(cantidad)
            
    def pedido_preparado(self):
        self.estado = "entregar"
    
    def pedido_entregado(self):
        self.estado = "entregado"
        
    def pedido_cobrado(self):
        self.estado = "cobrado"
        
    def ver_id(self):
        return self.id_pedido