from typing import TypeVar
T = TypeVar("T")

class GrafoConjunto():
    # Constructor de la clase, inicializa el grafo con conjuntos vacíos de vértices y aristas
    def __init__(self) -> None:
        self.nodos: set[T] = set()  # Conjunto de vértices o nodos del grafo
        self.aristas: dict[tuple[T, T], int] = {} # Conjunto de aristas, que son pares de vértices
    
    def agregar_nodo(self, nodo: T)->None:
        if nodo not in self.nodos:
            self.nodos.add(nodo)
        else:
            raise ValueError(f"El nodo {nodo} ya existe")
    
    def agregar_arista(self, origen: T, destino: T, peso: int)->None:
        if origen not in self.nodos:
            raise ValueError(f"El nodo {origen} no existe")
        
        elif destino not in self.nodos:
            raise ValueError(f"El nodo {destino} no existe")
        if (origen,destino) not in self.aristas:
            self.aristas[(origen,destino)] = peso
                
        else:
            raise ValueError(f"La arista {(origen,destino)} ya existe")
        
    
    def eliminar_arista(self, origen: T, destino: T) -> None:
        if (origen, destino) in self.aristas:
            del self.aristas[(origen, destino)]
        if (destino, origen) in self.aristas:
            del self.aristas[(destino, origen)]
    
    def eliminar_nodo(self, nodo: T)->None:
        if nodo in self.nodos:
            self.nodos.remove(nodo)
            for v in self.nodos:
                self.eliminar_arista(nodo, v)
        else:
            raise ValueError('nodo no existe en el grafo')
    
    def es_vecino_de(self, nodo: T, otro_nodo: T) -> bool:
        if ((nodo, otro_nodo) in self.aristas) or ((otro_nodo, nodo) in self.aristas):
            return True
        elif nodo not in self.nodos:
            raise ValueError(f"El nodo {nodo} no existe")
        
        elif otro_nodo not in self.nodos:
            raise ValueError(f"El nodo {otro_nodo} no existe")
        
        else:
            return False
    
    def vecinos_de(self, nodo: T) -> set[T]:
        vecinos: set[T] = set()
        if nodo not in self.nodos:
            raise ValueError(f"El nodo {nodo} no existe")
        
        for arista in self.aristas:
            if nodo in arista:
                for a in arista:
                    if a != nodo:
                        vecinos.add(a)
        return vecinos
    
    def dfs(self) -> list[T]:
        recorrido = []

        def dfs_interna(nodo: T):
            if nodo not in recorrido:
                recorrido.append(nodo)
                for vecino in self.vecinos_de(nodo):
                    dfs_interna(vecino)

        if not self.nodos:
            return [] # si no tiene nodos

        nodo_inicial = list(self.nodos)[0]
        dfs_interna(nodo_inicial)
        return recorrido
    
    def dijkstra(self, origen, destino):
        recorrido = []
        
        # print("nodos sin marcar: ", nodos_sin_marcar)
        etiquetas = {i: ["", float("inf")] for i in list(self.nodos)}
        etiquetas[origen] =["", 0]
        nodos_sin_marcar =list(self.nodos)

        while nodos_sin_marcar:
            nodo_actual = None
            min_distancia = float("inf")
            for n in nodos_sin_marcar:
                if etiquetas[n][1] < min_distancia:
                    min_distancia = etiquetas[n][1]
                    nodo_actual = n

            for vecino in self.vecinos_de(nodo_actual):
                if (nodo_actual, vecino) in self.aristas:
                    arista = (nodo_actual, vecino)
                else:
                    arista = (vecino, nodo_actual)
                peso = self.aristas[arista]
                nueva_distancia = etiquetas[nodo_actual][1] + peso

                if nueva_distancia < etiquetas[vecino][1]:
                    etiquetas[vecino] = [nodo_actual, nueva_distancia]
            
            nodos_sin_marcar.remove(nodo_actual)
        
        recorrido = []
        actual = destino
        while actual != "":
            recorrido.insert(0, actual)
            actual = etiquetas[actual][0]

        return recorrido, etiquetas[destino][1]

def main():
    migrafo = GrafoConjunto()
    migrafo.agregar_nodo("a")
    migrafo.agregar_nodo("b")
    migrafo.agregar_nodo("c")
    migrafo.agregar_nodo("d")
    migrafo.agregar_nodo("e")
    migrafo.agregar_nodo("f")
    print(list(migrafo.nodos))
    migrafo.agregar_arista("a","c",2)
    migrafo.agregar_arista("a","d",3)
    migrafo.agregar_arista("a","b",5)
    migrafo.agregar_arista("c","b",1)
    migrafo.agregar_arista("b","e",1)
    migrafo.agregar_arista("d","e",2)
    migrafo.agregar_arista("b","f",3)
    migrafo.agregar_arista("e","f",1)
    print("aristas: ", migrafo.aristas[("a","c")])

    print("recorrido minimo = ", migrafo.dijkstra("a","f"))

    
if __name__ == "__main__":
    main()