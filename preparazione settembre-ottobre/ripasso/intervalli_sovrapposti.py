
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:

    intervals = sorted(intervals) # ordino la lista di inervalli
    

    if intervals[-1][0] >= intervals[-1][1]: # se il primo numero dell'ultimo intervallo è maggiore del secondo inalzo un'eccezione
        
        raise ValueError("l'intervallo dell'ultimo elemento non è stato scritto nell'ordine corretto")

    for i in range(len(intervals[:-1])): # itero la lista degli intervalli  (escluso l'ultimo)
        
        if len(intervals[i]) != 2: # se l'intervallo non contiene due numeri allora inalzo un'eccezione

            raise ValueError("ogni intervallo deve contenere non più o meno di 2 valori")
        
        if intervals[i][0] >= intervals[i][1]: # se il primo numero di un intervallo i è maggiore del secondo allora inalzo un eccezione
            
            raise ValueError("l'intervallo non è scritto nell'ordine corretto")
        
        if i == len(intervals) - 1: # se i è uguale al valore dell'indice dell'ultimo elemento di intervals allora interrompo il ciclo con break
            break
        
        if intervals[i][1] in range(intervals[i + 1][0], intervals[i + 1][1] + 1): # se il secondo elemento di un intervallo i rientra tra l'intervallo degli elementi di i + 1 allora unisco i due intervalli nell'intervallo i 
            intervals[i] = [intervals[i][0], intervals[i + 1][1]]
            intervals.remove(intervals[i + 1]) # rimuovo l'intervallo i + 1 dato che si è unito al primo
        
    return intervals


    
    
    
    
        
def main():

    print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(merge_intervals([[1, 4], [4, 5]]))

main()