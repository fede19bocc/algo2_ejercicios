from typing import Callable

def wrapper(funcion: Callable) -> None:
    print(f"uso un wrapper para ejecutar {funcion.__name__}()")
    f()
   
def f() -> None:
    print("f() ejecutada ")

#%%
wrapper(f)
