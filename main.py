import itertools
from itertools import permutations

posibles_ordenes = itertools.permutations("DEF",)
for elemento in posibles_ordenes:
    print(elemento)