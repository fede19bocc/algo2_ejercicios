from Moto import Moto
from Auto import Auto

titan = Moto("Honda", "cg150", 1000)
clio = Auto("Renault", "Clio mio", 1200.01)
dias = 10

print(f"costo moto para {dias} es: {titan.calcularCostoalquiler(dias)}")
print(f"costo auto para {dias} es: {clio.calcularCostoalquiler(dias)}")