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





def merge_intervals(intervals: list [list[int]]):

    intervals = sorted(intervals)


    if intervals == []:

        return intervals
    
    elif len(intervals) == 1:

        return intervals
    

    mylist: list[list[int]] = [intervals[0]]

    
    for i in range(1, len(intervals)):

        if intervals[i][0] <= mylist[-1][1]:

            mylist[0][-1] = intervals[i][1]
        
        else:

            mylist.append(intervals[i])
    
    return mylist

    
        

    
    
    
    
        

    
    

        

        
    

        
        

        

        
    

    

        




test = merge_intervals([[1, 4], [4, 5]])


print(test)

    