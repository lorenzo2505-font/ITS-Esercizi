'''Utilizzare una list comprehension per convertire una lista di gradi Fahrenheit in gradi Celsius.'''


fahrenheit: list[float] = [f for f in range(1, 10 + 1)]

celsius: list[float] = [round((c - 32) * 5/9, 2) for c in fahrenheit]

print(celsius)
