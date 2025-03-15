# contar digitos
def contar_digitos(num: int) -> int:
    digitos = list(str(num))
    if len(digitos) == 1:
        return 1
    else:
        digitos.pop()
        num = int("".join(digitos))
        return contar_digitos(num) + 1
    
# print(contar_digitos(3456))

# da vuelva el numero
def reversa_num(num):
    if num < 10:
        return num 
    else:
        return reversa_num(num // 10)  + (num % 10) * 10 ** (len(str(num)) - 1) 
    
print(reversa_num(123))

# recursima de dado un numero entero retorne la suma de sus numeros

def suma_digitos(num):
    if num < 10:
        return num
    else:
        return suma_digitos(num // 10) + num % 10
    
print("suma_digitos", suma_digitos(1234))

# recursiva que devuelva dos valores a la vez de sumadigitos y reversion

def anonima(num):
    return (reversa_num(num), contar_digitos(num))
        
print("anonima", anonima(123))