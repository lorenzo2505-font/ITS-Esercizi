#return e print

def subtract (a, b):
    result = a - b
    return result #valore fornito

subtract(4, 1) #il valore non è stato preso

print(subtract(4,  1)) #il valore è stato preso e reso visualizzabile grazie a print()

#return omesso

def greet (name: str) -> None: 
    print(f"hello {name.title()}  !")

greet("angela")

print(type(greet("angela")))

#definire una funzione restituendo valore multipli ( e una tupla)

def op (a: int, b: int):
    sum_result: int = a + b
    diff_result: int = a - b
    #restituisce una tupla con due valori
    return sum_result, diff_result
#assegna il valore a due variabili
sum_value, diff_value = op (10, 5)

print(f"sum: {sum_value}")

print(f"difference: {diff_value}")

print(type(op(10,  5)))

#definire una funzione restituendo una lista

def coordinates (x: float, y: float):
    return [x, y]
coords = coordinates (12.5, 4.5)

print(coords[0], coords[1], sep = ", ")

print(type(coords))

#definire una lista restituendo un dizionario

def get_user (myname: str, myrole: str):
    return {"name": myname, "role": myrole}
user = get_user ("Alice", "Admin")

print(user["name"])
print(user["role"])
print(type(user))