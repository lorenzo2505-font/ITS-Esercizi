
def calculateCharges(periodo: int|float) -> str:

    m = periodo % 1

    if m > 0:

        periodo += 1 - m 
    
    #print(f"periodo: {periodo}")

    if periodo <= 3:

        tariffa = 2 

        return f"{tariffa}"
    
    elif periodo >= 24:

        tariffa = 10

        return f"{tariffa}"
    
    else:

        tariffa = 2 + ((periodo - 3) * 0.5)

        return f"{tariffa}"



'''cars: list[int] = [1, 2, 3, 4]

hours: list[float] = [1.5, 4.0, 5.5, 24.0]

changes: list = []

for i in range(4):

    t = calculateCharges(hours[i])

    changes.append(t)


print("car hours change")

for i in range(4):

    print(cars[i], hours[i], changes[i])'''





cars: list[float] = [1.5, 4.0, 5.5, 24.0]

totale = 0

print(f"{'car':<10}{'hours':<10}{'charges':<10}")

for i in range(len(cars)):

    t = calculateCharges(cars[i])

    print(f"{i + 1:<10}{cars[i]:<10}{t:<.2f}")

    totale += t

print(f"{totale:<10}{sum(cars):<10}{totale:<.2f}")


