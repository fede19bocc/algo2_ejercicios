from typing import TypeVar
import numpy as np
T = TypeVar("T")

class GrafoMatrizAdy():
    def __init__(self):
        self.matriz_adyacencia: list[list[int]] = []
        self.nodos: list[T] = []
    
    def agregar_nodo(self, valor_nodo: T):
        self.nodos.append(valor_nodo)
        self.matriz_adyacencia.append(np.zeros(len(self.nodos)))
        for i in range(len(self.matriz_adyacencia)-1):
            self.matriz_adyacencia[i] = np.append(self.matriz_adyacencia[i], 0)
            
            
    def agregar_arista(self, nodo1: T, nodo2: T):
        indice_nodo1 = self.nodos.index(nodo1)
        indice_nodo2 = self.nodos.index(nodo2)
        self.matriz_adyacencia[indice_nodo1][indice_nodo2] = 1
        self.matriz_adyacencia[indice_nodo2][indice_nodo1] = 1
    
    def eliminar_nodo(self, nodo: T):
        indice = self.nodos.index(nodo)
        self.nodos.remove(nodo)
        for i in range(len(self.matriz_adyacencia)):
            self.matriz_adyacencia[i] = np.delete(self.matriz_adyacencia[i], indice) 
        self.matriz_adyacencia.pop(indice)
        
    def eliminar_arista(self, nodo1: T, nodo2: T):
        indice_nodo1 = self.nodos.index(nodo1)
        indice_nodo2 = self.nodos.index(nodo2)
        self.matriz_adyacencia[indice_nodo1][indice_nodo2] = 0
        self.matriz_adyacencia[indice_nodo2][indice_nodo1] = 0
        
    def es_vecino_de(self, nodo1: T, nodo2: T) -> bool:
        indice_nodo1 = self.nodos.index(nodo1)
        indice_nodo2 = self.nodos.index(nodo2)
        arista = self.matriz_adyacencia[indice_nodo1][indice_nodo2]
        return arista == 1
    
    def vecinos_de(self, nodo: T)->list[T]:
        vecinos = []
        indice = self.nodos.index(nodo)
        pos_nodo = 0
        for i in self.matriz_adyacencia[indice]:
            if i == 1:
                vecinos.append(self.nodos[pos_nodo])
            pos_nodo += 1
        return vecinos
    
def main():
    migrafo = GrafoMatrizAdy()
    migrafo.agregar_nodo(1)
    migrafo.agregar_nodo(2)
    migrafo.agregar_nodo(3)
    migrafo.agregar_nodo(4)
    migrafo.agregar_arista(1,2)
    migrafo.agregar_arista(1,3)
    migrafo.agregar_arista(2,4)
    
    print("vecinos del nodo 2", migrafo.vecinos_de(2))
          
    for g in migrafo.matriz_adyacencia:
        print(g)
    print("Es vecino 2 de 3",migrafo.es_vecino_de(2,3))
    print("Es vecino 4 de 2",migrafo.es_vecino_de(4,2))
    
    print("elimino nodo 3 y arista 1-2")
    migrafo.eliminar_arista(1,2)
    migrafo.eliminar_nodo(3)
    for g in migrafo.matriz_adyacencia:
        print(g)
    print()
    
    print(migrafo.nodos)
    
    
#      1
#     / \
#  4-2   3     

if __name__ == "__main__":
    main()