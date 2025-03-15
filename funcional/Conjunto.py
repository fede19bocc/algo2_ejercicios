
class Conjunto:
    def __init__(self, valores):
        self.valores = tuple(valores)

    def __repr__(self):
        return f"valores = {self.valores}"
#%%

test = Conjunto([1,2,3])
print(test.valores[1])
print(test)

# test.valores[1] = "a"

test2 = Conjunto(["fede", 1, True, 1.12323])
print(test2)

#%%
def impura():
    print("Hola")

def pura():
    msj = impura()
    return msj

texto = impura()
print(texto)
# %%
