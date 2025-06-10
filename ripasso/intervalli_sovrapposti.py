'''Unione di Intervalli Sovrapposti

Data una lista di intervalli chiusi rappresentati come liste di due elementi [start, end],
scrivi una funzione merge_intervals(intervals) che restituisce una nuova lista di
intervalli in cui tutti quelli sovrapposti sono stati fusi. Ogni intervallo soddisfa start <=
end.

La lista risultante deve essere ordinata per inizio intervallo e non devono esserci
sovrapposizioni.


Requisiti:
● Input: una lista di liste, ad esempio [[1, 4], [2, 6], [8, 10], [15, 18]].

● Se due intervalli si sovrappongono o si toccano (es. [1,4] e [4,5]), unirli in
[1,5].

● Restituisci una lista di intervalli fusi, ordinata per il valore di inizio.
● Casi limite:
○ Se l’input è vuoto, restituisci una lista vuota.
○ Se è presente un solo intervallo, restituiscilo così com’è.


Esempi:

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals) # restituisce [[1, 6], [8, 10], [15,
18]]

intervals = [[1, 4], [4, 5]]
merge_intervals(intervals) # restituisce [[1, 5]]'''

import math



def merge_intervals(intervals: list [list[int]]):

    intervals = sorted(intervals)

    
    for i in range (len(intervals)):

        j = i + 1

        if (len(intervals[i]) != 2) or (intervals[i][0] > intervals[i][1]):

            raise Exception("ogni elemento deve avere due elementi con il primo minore del secondo")
        
        
        if intervals[i][1] in range(intervals[j][0], intervals[j][0]):

            return True
    
    
    
    
        

    
    

        

        
    

        
        

        

        
    

    

        




test = merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])


print(test)

    