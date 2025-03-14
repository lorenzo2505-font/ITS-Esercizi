def maximum (num1: int, num2: int):
    if num1 > num2:
        return num1
    else:
        return num2
#chiamare la funzione maximum
numMax: int = maximum(3, 4)
print(numMax)