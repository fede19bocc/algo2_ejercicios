class Viaje:
    
    def __init__(self, trayecto: Trayecto, vagones: int, pasajeros: int):
        self.trayecto = trayecto
        self.vagones = vagones
        self.pasajeros = pasajeros
    def tiempoDeDemora():
        pass

class Trayecto:
    
    def __init__(self, origen: str, destino: str, distancia: int, nro_estaciones: int):
        self.origen = origen
        self.destino = destino
        self.distancia = distancia
        self.nro_estaciones = nro_estaciones