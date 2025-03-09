class Monedero:
    
    def __init__(self, dinero):
        self.dinero = dinero
    
    def cargar_dinero(self, valor):
        self.dinero += valor
        print(f'Se agrego ${valor} a su cuenta')
    
    def retirar_dinero(self, valor):
        if valor > self.consultar_disponible():
            print("No posee suficientes fondos")
        else:
            self.dinero -= valor
            print(f'Se retira ${valor} de su cuenta')
    
    def consultar_disponible(self):
        return self.dinero
    
    def ver_disponible(self):
        print(f'Usted posee ${self.consultar_disponible()}')
    
#%%
print("creo nuevo monedero con 1000")
monedero = Monedero(1000)

monedero.cargar_dinero(500)
monedero.retirar_dinero(100)
monedero.ver_disponible()

print("pruebo falta de fondos, retirando $5000")
monedero.retirar_dinero(5000)    