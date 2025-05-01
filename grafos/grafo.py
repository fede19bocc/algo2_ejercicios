from typing import TypeVar
T = TypeVar("T")

class Grafo():
    # Constructor de la clase, inicializa el grafo con conjuntos vacíos de vértices y aristas
    def __init__(self, vertices: set[T] = set(), aristas: set[tuple[T, T]] = set()) -> None:
        self.vertices = vertices # Conjunto de vértices o nodos del grafo
        self.aristas = aristas # Conjunto de aristas, que son pares de vértices
    
    def agregar_nodo(self, nodo: T)->None:
        self.vertices.add(nodo)
    
    def agregar_arista(self, origen: T, destino: T)->None:
        self.aristas.add((origen,destino))
    
    def eliminar_arista(self, origen: T, destino: T) -> None:
        if (origen, destino) in self.aristas:
            self.aristas.remove((origen, destino))
        if (destino, origen) in self.aristas:
            self.aristas.remove((destino, origen))
    
    def eliminar_nodo(self, nodo: T)->None:
        if nodo in self.vertices:
            self.vertices.remove(nodo)
            for v in self.vertices:
                self.eliminar_arista(nodo, v)            
    
    def es_vecino_de(self, nodo: T, otro_nodo: T) -> bool:
        if (nodo, otro_nodo) in self.aristas or (otro_nodo, nodo) in self.aristas :
            return True     
        return False
    
    def vecinos_de(self, nodo: T) -> set[T]:
        vecinos = set()
        for arista in self.aristas:
            if nodo in arista:
                for a in arista:
                    if a != nodo:
                        vecinos.add(a)
        return vecinos
    
def main():
    migrafo = Grafo()
    migrafo.agregar_nodo(1)
    migrafo.agregar_nodo(2)
    migrafo.agregar_nodo(3)
    migrafo.agregar_nodo(4)
    migrafo.agregar_arista(1,2)
    migrafo.agregar_arista(1,3)
    migrafo.agregar_arista(2,4)
    print(migrafo.vertices)
    print(migrafo.aristas)
    print("Es vecino 2 de 3",migrafo.es_vecino_de(2,3))
    print("Es vecino 4 de 1",migrafo.es_vecino_de(4,1))
    migrafo.eliminar_nodo(2)
    print(migrafo.vertices)
    print(migrafo.aristas)
    
#      1
#     / \
#  4-2   3     
if __name__ == "__main__":
    main()