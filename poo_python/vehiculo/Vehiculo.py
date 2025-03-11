class Vehiculo:
    def __init__(self, marca: str, modelo: str, precioBase: int | float) -> None:
        self._marca = marca
        self._modelo = modelo
        self._precioBase = precioBase

    @property
    def precioBase(self) -> int | float:
        return self._precioBase
    
    @precioBase.setter
    def precioBase(self, valor: int | float) -> None:
        self._precioBase = valor

    def calcularCostoalquiler(self, dias: int) -> int | float:
        return self.precioBase * dias
    