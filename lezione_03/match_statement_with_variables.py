#variabili definite
g: str = "f"
age: int = 5

match(g, age):
    case("f", 5):
        print("piccola!")
    case("m", 5):
        print("piccolo!")
    case("f", 10):
        print("grande!")
    case("m", 10):
        print("gigante!")
    case _ :
        print("sorpresa!")
