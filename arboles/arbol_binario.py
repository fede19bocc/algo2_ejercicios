from collections.abc import Callable
from typing import Any, Generic, Optional, TypeVar
from functools import wraps

T = TypeVar('T')

class NodoAB(Generic[T]):
    def __init__(self, dato: T, si: "Optional[ArbolBinario[T]]" = None, sd: "Optional[ArbolBinario[T]]" = None):
        self.dato = dato
        self.si: ArbolBinario[T] = ArbolBinario() if si is None else si
        self.sd: ArbolBinario[T] = ArbolBinario() if sd is None else sd

    def __str__(self):
        return self.dato
    
class ArbolBinario(Generic[T]):
    def __init__(self):
        self.raiz: Optional[NodoAB[T]] = None
        
    class _Decoradores:
        @classmethod
        def valida_es_vacio(cls, f: Callable[..., Any]) -> Callable[..., Any]:
            @wraps(f)
            def wrapper(self, *args: Any, **kwargs: Any) -> Any:
                if self.es_vacio():
                    raise TypeError('Arbol Vacio')
                return f(self, *args, **kwargs)
            return wrapper
        
    @staticmethod
    def crear_nodo(dato: T, si: "Optional[ArbolBinario[T]]" = None, sd: "Optional[ArbolBinario[T]]" = None) -> "ArbolBinario[T]":
        t = ArbolBinario()
        t.raiz = NodoAB(dato, si, sd)
        return t

    def es_vacio(self) -> bool:
        return self.raiz is None
    
    @_Decoradores.valida_es_vacio
    def si(self) -> "ArbolBinario[T]":
        assert self.raiz is not None
        return self.raiz.si
    
    @_Decoradores.valida_es_vacio
    def sd(self) -> "ArbolBinario[T]":
        assert self.raiz is not None
        return self.raiz.sd
    
    def es_hoja(self) -> bool:
        return not self.es_vacio() and self.si().es_vacio() and self.sd().es_vacio()

    @_Decoradores.valida_es_vacio
    def dato(self) -> T:
        assert self.raiz is not None
        return self.raiz.dato
    
    @_Decoradores.valida_es_vacio
    def insertar_si(self, si: "ArbolBinario[T]"):
        assert self.raiz is not None
        self.raiz.si = si

    @_Decoradores.valida_es_vacio
    def insertar_sd(self, sd: "ArbolBinario[T]"):
        assert self.raiz is not None
        self.raiz.sd = sd

    def set_raiz(self, nodo: NodoAB[T]):
        self.raiz = nodo
        
    def altura(self) -> int:
        if self.es_vacio():
            return 0
        else:
            return 1 + max(self.si().altura(), self.sd().altura())
        
    def __len__(self) -> int:
        if self.es_vacio():
            return 0
        else:
            return 1 + len(self.si()) + len(self.sd())
    
    def __str__(self):
        def mostrar(t: ArbolBinario[T], nivel: int):
            tab = '.' * 4
            indent = tab * nivel
            if t.es_vacio():
                return indent + 'AV\n'
            else:
                out = indent + str(t.dato()) + '\n'
                out += mostrar(t.si(), nivel + 1)
                out += mostrar(t.sd(), nivel + 1)
                return out
            
        return mostrar(self, 0)

    def inorder(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return self.si().inorder() + [self.dato()] + self.sd().inorder()
    
    def inorder_tail(self) -> list[T]:
        pass

    def preorder(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return [self.dato()] + self.si().inorder() +  self.sd().inorder()

    def posorder(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return  self.si().inorder() +  self.sd().inorder() + [self.dato()]

    def bfs(self) -> list[T]:
        # revisar pincha insertar en arbol_binario_ordenado
        # lo toma vacio al arbol
        if self.es_vacio():
                return []
        orden = [self.dato()]
        actual =[self.si(), self.sd()]
        while actual:
            nodo = actual.pop(0)
            orden.append(nodo.dato())
            if not nodo.si().es_vacio():
                actual.append(nodo.si())
            if not nodo.sd().es_vacio():
                actual.append(nodo.sd())
        return orden

    
    def nivel(self, dato: T) -> int:
        if self.es_vacio():
            return -1
        
        cola = [(self, 1)]
        
        while cola:
            actual, nivel_actual = cola.pop(0)
            if actual.dato() == dato:
                return nivel_actual
            if not actual.si().es_vacio():
                cola.append((actual.si(), nivel_actual + 1))
            if not actual.sd().es_vacio():
                cola.append((actual.sd(), nivel_actual + 1))
        
        return -1

    def copy(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            return ArbolBinario()
        else:
            nuevo = ArbolBinario()
            nuevo.set_raiz(NodoAB(self.dato()))
            nuevo.insertar_si(self.si().copy())
            nuevo.insertar_sd(self.sd().copy())
            return nuevo

    def espejo(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            return ArbolBinario()
        else:
            espejado = ArbolBinario()
            espejado.set_raiz(NodoAB(self.dato()))
            espejado.insertar_si(self.sd().copy())
            espejado.insertar_sd(self.si().copy())
            return espejado
        
    def sin_hojas(self):
        if self.es_vacio():
            return ArbolBinario()
        else:
            sin_hoja = ArbolBinario()
            sin_hoja.set_raiz(NodoAB(self.dato()))
            if not self.si().es_hoja():
                sin_hoja.insertar_si(self.si().sin_hojas())
            if not self.sd().es_hoja():
                sin_hoja.insertar_sd(self.sd().sin_hojas())
            return sin_hoja
        

def main():
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4   5 6   7
    #      /
    #     8
    t = ArbolBinario.crear_nodo(1)
    n2 = ArbolBinario.crear_nodo(2)
    n3 = ArbolBinario.crear_nodo(3)
    n4 = ArbolBinario.crear_nodo(4)
    n5 = ArbolBinario.crear_nodo(5)
    n6 = ArbolBinario.crear_nodo(6)
    n7 = ArbolBinario.crear_nodo(7)
    n8 = ArbolBinario.crear_nodo(8)
    n2.insertar_si(n4)
    n2.insertar_sd(n5)
    n5.insertar_si(n8)
    n3.insertar_si(n6)
    n3.insertar_sd(n7)
    t.insertar_si(n2)
    t.insertar_sd(n3)
    
    print("visualizacion del arbol")
    print(t)

    print(f'Altura: {t.altura()}')
    print(f'Nodos: {len(t)}')

    print(n3)
    print(f'largo n3: {len(n3)}')
    print(f'DFS inorder: {t.inorder()}')
    print(f'DFS preorder: {t.preorder()}')
    print(f'DFS postorder: {t.posorder()}')

    print(f'BFS: {t.bfs()}')
    print(f'Nivel de 8: {t.nivel(8)}')
    
    t2 = t.copy()
    print(f'imprimo copia \n', t2)
    print(f'DFS inorder stack: {t2.inorder()}')
    print(f'DFS inorder tail:  {t2.inorder_tail()}')
    print(f'Nivel de 8: {t2.nivel(8)}')

    t3 = t2.espejo()
    print("espejo: ")
    print(t3)
    print("sin hojas: ")    
    print(t3.sin_hojas())

if __name__ == '__main__':
    main()