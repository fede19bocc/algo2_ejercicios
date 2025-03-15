from collections import namedtuple
from dataclasses import dataclass

OtroConjunto = namedtuple("OtroConjunto", "nombre lista")

test = OtroConjunto("pepe", [1,2,3])

print(test)
print(type(test))

print(test[0])