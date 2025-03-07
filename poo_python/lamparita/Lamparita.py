class Lamparita:
    contador_lamparitas = 0
     
     
    # 0 es apagado, 1 encendido
    def __init__(self, estado = 0):
        self.estado = estado
        Lamparita.contador_lamparitas += 1

    def encender(self):
        self.estado = 1

    def apagar(self):
        self.estado = 0
    
    def verEstado(self):
        if self.estado == 1:
            print("Encendida!")
        else:
            print("Apagada!")
            
    @classmethod #sin el decorador no funciona
    def lamparitas_creadas(cls):
        return cls.contador_lamparitas

#%%
print("inicio lamparita, por defecto apagada")
lamparita = Lamparita()
lamparita.verEstado()

print("enciendo la lamparita")
lamparita.encender()
lamparita.verEstado()

print("apago la lamparita")
lamparita.apagar()
lamparita.verEstado()

print("lamparitas creadas")
print(Lamparita.lamparitas_creadas())
print(lamparita.lamparitas_creadas())