
# struttura -> lambda arguments: espressione

add = lambda a: a + 1

print(add(5))

mult = lambda a, b : a*b

print(mult(-5, 7))

# ESERCIZIO

# creare una funzione lambda che calcola il valore assoluto di un numero


'''valore_assoluto = lambda n: abs(n)''' # soluzione mia

absolute = lambda a : a if a >= 0 else -a

print(absolute(-1))
