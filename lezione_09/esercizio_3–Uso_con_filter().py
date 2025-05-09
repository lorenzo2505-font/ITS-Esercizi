'''Hai la seguente lista numeri = [5, 12, 17, 18, 24, 32]. Usa filter() con una lambda per ottenere solo i numeri pari.'''

from typing import Callable

numeri: list [int] = [5, 12, 17, 18, 24, 32]

pari: list [int] = list(filter(lambda i: i % 2 == 0, numeri))

print(pari)

