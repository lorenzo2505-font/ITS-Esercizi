'''Crea una funzione che converta un dato numero intero nella sua rappresentazione in numeri romani.

Gestisci numeri da 1 a 3999.

Utilizza una combinazione di manipolazione di stringhe e istruzioni condizionali per costruire il numero romano.'''


def convertiInRomano(n: int) -> str:
    numero_romano: str = "" # inizializzo il numero romano come una stringa vuota

    if not(1 <= n <= 3999): # se il numero non è compreso tra 1 e 3999 mando il programma in errore

        raise ValueError("il numero deve avere un valore compreso tra 1 e 3999")
    
    arabi: list[int] = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] # creao una lista contenente dei numeri arabi
    romani: list[str] = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"] # creo una lista contenenti i numeri romani corrispettivi ai numeri arabi nella lista precedente

    for i in range(len(arabi)): # ciclo solo la lista degli arabi(ha una lista identica a quella dei romani)

        while n >= arabi[i]: # finche il numero è maggiore uguale all'elemento i della lista degli arabi lo sottraggo all'elemento i, e aggiungo alla stringa numero_romano il corrispettivo romano
            n -= arabi[i]
            numero_romano += romani[i]
        
    
    return numero_romano

print(convertiInRomano(2005))



    