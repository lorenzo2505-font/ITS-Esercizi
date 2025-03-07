#parametri passati di posizione

def describe_person (name: str, age: int, city: str):
    print(f"{name} is {age} years old and lives in {city}")

describe_person ("Alice", 25, "Roma")

#quando gli argomenti sono passati per posizione, gli argomenti nell'istruzione di chiamata sono abbinati ai parametri della funzione, ciò significa che si basano sul loro ordine 

