'''Dato un array di numeri interi nums e un intero target, restituisci gli indici dei due numeri in modo che la loro somma dia come target.

Puoi supporre che ogni input abbia esattamente una soluzione e non puoi utilizzare lo stesso elemento due volte.

Puoi restituire la risposta in qualsiasi ordine.'''

def two_sum(mylist: list[int], target: int) -> list[int] | None:

    index = 0
    somma = 0
    newlist: list[int] = []

    for i in mylist:
        newlist.append(i)

    while True:
        newlist.pop(index)
        
        for n in range(len(newlist)):
            somma = mylist[index] + newlist[n]

            if somma == target:
                return [index, n + 1]
            
            else:
                somma = 0
                continue
        
        if somma != target:
            newlist.insert(index, mylist[index])
            index += 1
        
        if index >= len(mylist):
            break
    
    return None
        
        

print(two_sum([2,7,11,15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))