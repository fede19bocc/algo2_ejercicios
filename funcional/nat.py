from typing import Union, TypeAlias

__all__ = ['Nat', 'cero', 'division', 'es_cero', 'igual', 'mayor', 'mayor_igual', 'menor', 'menor_igual', 'nat_to_int', 'potencia', 'pred', 'producto', 'resta', 'suc', 'suma']

Nat: TypeAlias = Union["Cero", "Suc"]

# Clases constructoras de estructura
class Cero:
    def __repr__(self):
        return 'Cero'

    def __str__(self):
        return '0'
    
    def __eq__(self, otro: Nat):
        return es_cero(otro)
    
    def __lt__(self, otro: Nat):
        return not es_cero(otro)
    
    def __add__(self, otro: Nat):
        return otro
    
    def __mul__(self, otro: Nat):
        return self

class Suc:
    def __init__(self, pred: Nat):
        self.pred = pred

    def __repr__(self):
        if isinstance(self.pred, Cero):
            return 'Suc(Cero)'
        else:
            return f'Suc({self.pred.__repr__()})'

    def __str__(self):
        return str(nat_to_int(self))
    
    def __eq__(self, otro: Nat):
        return igual(self, otro)
    
    def __lt__(self, otro: Nat):
        return menor(self, otro)
    
    def __gt__(self, otro: Nat):
        return mayor(self, otro)
    
    def __add__(self, otro: Nat):
        return suma(self, otro)
    
    def __mul__(self, otro: Nat):
        return producto(self, otro)

# Operaciones
def cero() -> Nat:
    return Cero()

def es_cero(n: Nat) -> bool:
    return isinstance(n, Cero)

def suc(n: Nat) -> Nat:
    return Suc(n)

def pred(n: Nat) -> Nat:
    if es_cero(n):
        raise ValueError('cero no tiene predecesor')
    else:
        return n.pred

def nat_to_int(n: Nat) -> int:
    if es_cero(n):
        return 0
    else:
        return 1 + nat_to_int(pred(n))

def suma(x: Nat, y: Nat) -> Nat:
    if es_cero(x):
        return y
    else:
        return suma(pred(x), suc(y))
    
def igual(x: Nat, y: Nat) -> bool:
    if es_cero(x):
        return es_cero(y)
    elif es_cero(y):
        return False
    else:
        return igual(pred(x), pred(y))
    
def menor(x: Nat, y: Nat) -> bool:
    if es_cero(x) and es_cero(y):
        return False
    elif es_cero(x):
        return not es_cero(y)
    elif es_cero(y):
        return es_cero(x)
    else:
        return menor(pred(x), pred(y))
    
def mayor(x: Nat, y: Nat) -> bool:
    if es_cero(x):
        return es_cero(y)
    elif es_cero(y):
        return not es_cero(x)
    else:
        return mayor(pred(x), pred(y))

def menor_igual(x: Nat, y: Nat) -> bool:
    if es_cero(x) and es_cero(y): # 0, 0
        return True
    elif es_cero(x): # 0, 1
        return not es_cero(y)
    elif es_cero(y): # 1, 0
        return es_cero(x)
    else:
        return menor_igual(pred(x), pred(y))

def mayor_igual(x: Nat, y: Nat) -> bool:
    if es_cero(x) and es_cero(y): # 0, 0
        return True
    elif es_cero(x): # 0, 1
        return es_cero(y)
    elif es_cero(y): # 1, 0
        return not es_cero(x)
    else:
        return mayor_igual(pred(x), pred(y))

def resta(x: Nat, y: Nat) -> Nat:
    if es_cero(y):
        return x
    else:
        return resta(pred(x), pred(y))
    
def producto(x: Nat, y: Nat) -> Nat:
    if es_cero(y) or es_cero(x):
        return cero()
    elif y == suc(cero()):
        return x        
    else:
        return x + producto(x, pred(y))
    
def division(x: Nat, y: Nat) -> Nat:
    if es_cero(y):
        raise ValueError(f'No se puede dividir por {nat_to_int(y)}')
    elif  menor(x, y):
        return cero()
    else:
        return suma(suc(cero()), division(resta(x, y), y))

def potencia(base: Nat, exponente: Nat) -> Nat:
    if es_cero(exponente):
        return suc(cero())
    elif igual(exponente, suc(cero())):
        return base
    else:
        return producto(base, potencia(base, pred(exponente)))

if __name__ == '__main__':
    n1: Nat = cero()                # n1 = 0
    n2: Nat = suc(suc(suc(n1)))     # n2 = 3
    n3: Nat = suc(suc(n2))          # n3 = 5
    print(es_cero(n1))              # True
    n2 = pred(n2)                   # n2 = 2
    n2bis = suc(suc(n1))
    print("n2 == n2bis", n2 == n2bis)
    print("igual(n2, n2bis)", igual(n2, n2bis))
    print(n2)                       # 2
    print(n3)                       # 5
    n4: Nat = suma(n2, n3)          # n4 = 7
    print(n4)                       # 7
    print("cero + n4: ", n1 + n4)
    print("resta: ", resta(n4, n2))            # 7 - 2 = 5
    print(repr(n4)) # Suc(Suc(Suc(Suc(Suc(Suc(Suc(Cero)))))))
    
    print(f'n2 < n4: {n2 < n4}')
    print(f'n2 menor n4: {menor(n2, n4)}')
    print(f'n4 menor n2: {menor(n4, n2)}')
    
    print(f'0 < 0: {n1 < n1}')
    print(f'0 < 7: {n1 < n4}')
    
    print(f'n4 mayor n3: {mayor(n4, n3)}')
    print(f'n4 > n3: {n4 > n3}')
    
    print(f'producto(2, 7): {producto(n2, n4)}')  # 14
    print(f'producto(7, 2): {producto(n4, n2)}')  # 14
    print(f'2*7: {n2 * n4}')  # 14
    print(f'0*7: {cero() * n4}')  # 14
    
    print(f'n2 mayor igual n4: {mayor_igual(n2, n4)}') # n4=7 , n2=2
    print(f'n2 menor igual n2: {menor_igual(n2, n2)}')
    print(f'n4: {n4}, n2: {n2}')
    print(f'division(n4, n2): {division(n4, n2)}')  # 2
    n5: Nat = suc(n2)
    print(n5)
    print(f'potencia(n4, n5): {potencia(n2, n4)}')  # 2