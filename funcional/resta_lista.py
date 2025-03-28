def resta_lista(xs: list[int]) -> int:
    def apilado(xs: list[int], pila: list[int]):
        if xs != []:
            pila.append(xs[0])
            apilado(xs[1:], pila)

    def desapilado(pila: list[int], acumulador: int) -> int:
        if pila == []:
            return acumulador
        else:
            return desapilado(pila, pila.pop() - acumulador)
      
    pila = []
    apilado(xs, pila)
    return desapilado(pila, 0)

# def resta_lista_iterativa(xs: list[int]) -> int:
#      def apilado(xs: list[int], pila: list[int]):
        
#         if xs != []:
#             pila.append(xs[0])
#             apilado(xs[1:], pila)

#     def desapilado(pila: list[int], acumulador: int) -> int:
#         if pila == []:
#             return acumulador
#         else:
#             return desapilado(pila, pila.pop() - acumulador)
      
#     pila = []
#     apilado(xs, pila)
#     return desapilado(pila, 0)


print(resta_lista([10, 2, 5, 9])) # (10 - (2 - (5 - 9)) = 4
