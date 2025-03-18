def es_par(n: int) -> bool:
    """Dado un entero devuelve si es o no par"""
    return abs(n) == 0 or es_impar(abs(n) - 1)

def es_impar(n: int) -> bool:
    """Dado un entero devuelve si es o no impar"""
    return False if abs(n) == 0 else es_par(abs(n) -1)
    
print(es_par(-10))
print(es_impar(-4))

#%%
def pares(n: int) -> None:
    def encontrar_pares(x: int, y: int) -> None:
        if y > x:
            return
        if x + y == n:
            print(f"({y}, {x})")
        encontrar_pares(x-1, y+1)
    encontrar_pares(n-1, 1)
    
pares(5)
print("----")
pares(10)
# %%
def desde_hasta(i: int, n:int) -> list[int]:
   if i > n: # Caso base: si el inicio es mayor que el final entonces devuelvo una lista vacía.
       return []
   else:
       return [i] + desde_hasta(i+1, n)  # Agregar el primer número y continuar con la recursión.
   
a = desde_hasta(1,5)
b = desde_hasta(7,5)
c = desde_hasta(4,6)

print(a)
print(b)
print(c)