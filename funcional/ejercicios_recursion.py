def desde_hasta(i: int, n:int, lista=None) -> list[int]:
   # print("1,",lista)
   if lista is None: 
       lista = []

   if i > n: # Caso base: si el inicio es mayor que el final entonces devuelvo una lista vacía.
       return lista
   else:
       lista.append(i) # al usar el append seria una recursion de pila. hay que usar lista + [i]. Sumar dos listas
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
# suma_resta_alternada([1, 2,3, 4, 5]) = 1 + 2 - 3 + 4 - 5 = -1

def suma_resta_alternada(lista: list[int]) -> int:
    if not lista:
        return 0
    def interna(lista: list[int], resultado=0, indice=0) -> int:
        if not lista:
            return resultado
        if indice % 2 == 0:
            resultado += lista[0]
        else:
            resultado -= lista[0]
        return interna(lista[1:], resultado, indice + 1)
    return interna(lista[1:], lista[0])

print("suma resta alternada: ",  suma_resta_alternada([1, 2, 3, 4, 5]))
print("suma resta alternada: ",  suma_resta_alternada([]))
# %% ejercicio 5 bonus, hacerla iterativa

def suma_resta_alt_iter(lista: list[int]) -> int:
    if not lista:
        return 0  # Si la lista está vacía, devolvemos 0

    resultado = lista[0]  # Usamos el primer elemento como base
    i = 1  # Empezamos desde el segundo elemento

    while i < len(lista):
        if i % 2 == 1:  # Si el índice es impar, restamos
            resultado += lista[i]
        else:  # Si el índice es par, sumamos
            resultado -= lista[i]
        i += 1  # Avanzamos al siguiente índice
    
    return resultado
print("suma resta alt iterativa: ",  suma_resta_alt_iter([1, 2, 3, 4, 5]))
print("suma resta alt iterativa: ",  suma_resta_alt_iter([]))


# %% ejercicio 6

def sumar_digitos(num:int) -> int:
    def interna(num: int, suma = 0) -> int:
        if num < 10:
            return suma + num
        else:
            return interna(num // 10, suma + num % 10)
    return interna(num)

print("sumar digitos recursiva cola: ", sumar_digitos(4))

def sumar_digitos_iter(num: int) -> int:
    suma = num % 10
    while num > 10:
        num = num // 10
        suma += num % 10
    return suma

print("suma dig iter: ", sumar_digitos_iter(1))
# %% 
# ejercicio 7 Implementa una función que invierta una
# cadena utilizando recursión de cola
def invierte_cadena(cadena: str) -> str:
    def interna(cadena: str, invertida="") -> str:
        if len(cadena) < 1:
            return invertida
        else:
            return interna(cadena[:-1], invertida + cadena[-1])
    return interna(cadena)

print("invierto: ", invierte_cadena("ho"))
# %%
# ejercicio 7 iterativo
def invierte_cad_iter(cadena: str) -> str:
    invertida = ""
    while len(cadena) > 0:
        invertida += cadena[-1]
        cadena = cadena [:-1]
    return invertida

print("invierto iterativo: ", invierte_cad_iter("hola"))

# %%
# Implementar la recursión de cola de Fibonacci
def fibo(n: int) -> int:
    def fibo_interna(n: int, a=0, b=1) -> int:
        if n == 0:
            return a
        if n == 1:
            return b
        return fibo_interna(n-1, b, a + b)
    return fibo_interna(n)

fibo(4)

# %%
# calcular el producto de dos números enteros utilizando
# recursión de cola.

def producto(x: int, y: int) -> int:
    if x == 0 or y == 0:
        return 0
    def interna(x: int, y: int, acum: int) -> int:
        if y == 1:
            return acum
        else:
            return interna(x, y-1, acum + x)
    return interna(x, y, x)

print("producto recursivo cola ",producto(0,1))
# %%
