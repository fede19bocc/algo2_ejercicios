from Vehiculo import Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, precioBase):
        super().__init__(marca, modelo, precioBase)
    
    def calcularCostoalquiler(self, dias):
        return super().calcularCostoalquiler(dias) * 1.2
    