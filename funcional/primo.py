from collections.abc import Iterator

def impar(contador: int) -> Iterator[int]:
        while True:
            yield contador
            contador += 2

def generar_primo() -> Iterator[int]:
    posible_primo = impar(1)
    valor = next(posible_primo)
    primo = 0
    for i in range(valor, valor**2, 1):
        if valor % i == 0:
             primo = valor
    if primo == valor:
         yield primo

valor = generar_primo()

print(next(valor))