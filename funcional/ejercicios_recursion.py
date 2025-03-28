def desde_hasta(i: int, n:int, lista=None) -> list[int]:
   # print("1,",lista)
   if lista is None:
       lista = []

   if i > n: # Caso base: si el inicio es mayor que el final entonces devuelvo una lista vacía.
       return lista
   else:
       lista.append(i)
       # print("2", lista) 
       return desde_hasta(i+1, n, lista)  # Agregar el primer número y continuar con la recursión.
   
a = desde_hasta(1,3)
b = desde_hasta(7,5)
c = desde_hasta(4,6)

print(f"a, {a}")
print(f"b, {b}")
print(f"c, {c}")

# puse lista = [] en la firma pero quedaba guardada esa lista para las llamadas siguientes
#%% ejercicio 3

def intercalar(lista1: list[int], lista2: list[int], intercalada=None) -> list[int]:
    if len(lista1) == 0 and len(lista2) == 0:
        return []
    elif len(lista1) == 0 and len(lista2) != 0:
        return [lista2[0]] + intercalar([], lista2[1:])
    elif len(lista2) == 0 and len(lista1) != 0:
        return [lista1[0]] + intercalar(lista1[1:], [])
    else:
        return [lista1[0]] + [lista2[0]] + intercalar(lista1[1:], lista2[1:])

lista1 = [0,2,4]
lista2 = [1,3,5]

print(intercalar(lista1, lista2))

a = [0,2,4]
b = [1]

print(intercalar(a, b))

b = [0,2,4]
a = [1]

print(intercalar(a, b))

#%% ejercicio 4
def longitud_NO_recursiva(lista:list[int], contador=0) -> int:
    nueva = lista.copy()
    while nueva:
        contador += 1
        nueva = nueva[1:]
    return contador

c = [1,2,3,4]
d = c[1:]
print(longitud_NO_recursiva(c))

#%% ejercicio 5
# suma_resta_alternada([1, 2,3, 4, 5]) = 1 + 2 - 3 + 4 - 5

def suma_resta_alternada(lista: list[int], acumulador: int) -> None:
 pass