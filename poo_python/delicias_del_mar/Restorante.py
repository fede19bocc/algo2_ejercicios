class Restorante:
    contador_sucursales = 0
    
    def __init__(self, nombre, ciudad, nro_empleados):
        self.nombre = nombre
        self.ciudad = ciudad
        self.nro_empleados = nro_empleados
        Restorante.contador_sucursales += 1
    
    @classmethod
    def obtener_numero_sucursales(cls):
        return cls.contador_sucursales
    
    def calcular_costo_operativo(self, empleado_promedio):
        return self.nro_empleados * empleado_promedio
    
    
#%% test

pepes = Restorante("Pepes", "Buenos Aires", 10)
il_gato = Restorante("Il Gato", "Cordoba", 50)
nump = Restorante("Nump", "CABA", 15)

print(f'Cantidad de sucursales {Restorante.obtener_numero_sucursales()}')
print(f'Costo de {pepes.nombre} es ${pepes.calcular_costo_operativo(2000)} por mes')    
