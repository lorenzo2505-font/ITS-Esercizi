#parametri passati per parola chiave

def describe_person (name: str, age: int, city: str):
    print(f"{name} is {age} years old and lives in {city}")

describe_person (age = 25, city = "Roma", name = "Alice")

