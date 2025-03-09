class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def asignar_coordenadas(self, valor_x, valor_y):
        self.x = valor_x
        self.y = valor_y
        
    def obtener_coordenadas(self):
        return self.x, self.y
    
    @classmethod
    def sumar_puntos(cls, a, b):
        datos_a = a.obtener_coordenadas()
        datos_b = b.obtener_coordenadas()
        return Punto(datos_a[0] + datos_b[0], datos_a[1] + datos_b[1])
    
    def __eq__(self, punto):
        return isinstance(punto, Punto) and self.x == punto.x and self.y == punto.x
    
    def __hash__(self):
        return hash(self.x, self.y)
    
#%%
A = Punto(0,1)
B = Punto(1,1)

print(A.obtener_coordenadas())

C = Punto.sumar_puntos(A,B)
print(C.obtener_coordenadas())

D = Punto(0,0)
print("D = ", D.obtener_coordenadas())
D.asignar_coordenadas(1,1)
print("D = ", D.obtener_coordenadas())

print(B == A)