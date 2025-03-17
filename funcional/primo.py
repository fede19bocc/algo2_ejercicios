from collections.abc import Iterator

def impar(contador: int = 3) -> Iterator[int]:
    while True:
        yield contador
        contador += 2

def generar_primo() -> Iterator[int]:
    yield 2  # Primer número primo
    posible_primo = impar()
    for valor in posible_primo:
        if es_primo(valor):
            yield valor

def es_primo(numero: int) -> bool:
    if numero < 2:
        return False
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False
    return True

generador = generar_primo()
for i in range(20):
    print(next(generador))