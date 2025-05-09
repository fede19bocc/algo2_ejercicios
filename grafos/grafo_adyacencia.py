from typing import TypeVar
T = TypeVar("T")

class GrafoAdy():
    def __init__(self):
    # Inicializa el grafo como un diccionario donde las claves son nodos y los valores son conjuntos de nodos vecinos
        self.lista_adyacencia: dict[T, set[T]] = {}
    
    def nodos(self) -> list[T]:
        return list(self.lista_adyacencia.keys())
    
    def es_nodo(self, nodo: T) -> bool:
        return nodo in self.lista_adyacencia.keys()
    
    def agregar_nodo(self, nodo: T):
        if not self.es_nodo(nodo):
            self.lista_adyacencia[nodo] = set()
        
    def agregar_arista(self, origen: T, destino: T):
        if origen in self.lista_adyacencia.keys() and destino in self.lista_adyacencia.keys():
            self.lista_adyacencia[origen].add(destino)
        else:
            raise ValueError(f'{origen} o {destino} no son nodos del grafo')
            
    def eliminar_arista(self, origen: T, destino: T):
        if (self.es_nodo(origen)) and (destino in self.lista_adyacencia[origen]):
            self.lista_adyacencia[origen].remove(destino)
        elif (self.es_nodo(destino)) and (origen in self.lista_adyacencia[destino]):
            self.lista_adyacencia[destino].remove(origen)
        else:
            raise ValueError(f'La arista ({origen},{destino}) no existe en el grafo')
            
    def eliminar_nodo(self, nodo: T):
        if self.es_nodo(nodo):
            del self.lista_adyacencia[nodo] # elimino el nodo
            for llave in self.lista_adyacencia.keys(): # recorro las aristas y elimino de la lista de adyacencia
                if nodo in self.lista_adyacencia[llave]:
                    self.lista_adyacencia[llave].remove(nodo)
        else:
            raise ValueError(f'El nodo {nodo} no pertenece al grafo')
        
    def es_vecino_de(self, nodo: T, otro_nodo: T) -> bool:
        if nodo in self.lista_adyacencia.keys():
            return otro_nodo in self.lista_adyacencia[nodo]
        return False
    
    def vecinos_de(self, nodo: T) -> list[T]:
        if nodo in self.lista_adyacencia.keys():
            return self.lista_adyacencia[nodo]
        

def main():
    migrafo = GrafoAdy()
    migrafo.agregar_nodo(1)
    migrafo.agregar_nodo(2)
    migrafo.agregar_nodo(3)
    migrafo.agregar_nodo(4)
    migrafo.agregar_arista(1,2)
    migrafo.agregar_arista(1,3)
    migrafo.agregar_arista(2,4)
    print(migrafo.lista_adyacencia)
    print("Es vecino 2 de 3",migrafo.es_vecino_de(2,3))
    print("Es vecino 4 de 1",migrafo.es_vecino_de(4,1))
    # print("elimino arista (4,2)")
    # migrafo.eliminar_arista(4,2)
    # print("elimino nodo 5")
    # migrafo.eliminar_nodo(5)
    print(migrafo.lista_adyacencia)
    print(migrafo.lista_adyacencia.keys())
    print("es nodo 5: ", migrafo.es_nodo(5))
    
    
#      1
#     / \
#  4-2   3     

if __name__ == "__main__":
    main()