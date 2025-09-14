def isDna(s: str) -> bool: # funzione per verificare la validità delle sequenze di dna

    biolist: list[str] = ["A", "C", "T", "G"] # lista contente tutti caratteri possibili che può avere la sequenza di dna

    for i in s: # itero la stringa

        if i not in biolist: # se i non è nella lista contenente tutti i caratteri possibili allora ritorno False

            return False
    
    return True # se tutto va bene ritorno True

def individua_sovrapposizioni(s1: str, s2: str): # funzione per verificare la sovrapposizione delle sequenze
    
    test_s1 = isDna(s1) # testo la validità della prima sequenza
    test_s2 = isDna(s2) # testo la validità della seconda sequenza

    first_index = -1 # inizializzo una variabile uguale a -1
    second_index = 0 # inizializzo una variabile uguale a zero
    spaces: str = " " # inizializzo una stringa contenente solo uno spazio

    if test_s1 and test_s2: # se entrambi i test hanno i valori di True si continua con la risoluzione del problema

        while True: # ciclo infinito

            if s1 == s2: # se le due stringhe sono uguali allora si è trovata subito la sovrapposizione
                print("sovrapposizione trovata, le due sequenze di dna sono uguali")
                print(s1)
                print(s2)
                
                return f"lunghezza di sovrapposizione: {len(s1)}" # ritorno la lunghezza della sovrapposizione
            
            elif s1[first_index] != s2[0]: # se l'ultimo indice di s1(rappresentato da first_indedx) è diverso dal primo della seconda stringa allora incremento(o decremento il valore dei due indici)
                first_index -= 1
                second_index += 1
            
            else:

                if s1[first_index: ] == s2[ :second_index + 1]: # se la prima stringa(partendo dal valore del primo indice) è uguale alla seconda stringa(partendo dal valore del secondo indice) allora si è trovata la sovrapposizione
                    print("sovrapposizione trovata")
                    print(s1)
                    print(f"{spaces * len(s1[first_index: ])}{s2}") # si cerca di far combaciare le sovrapposizioni
                    
                    return f"lunghezza di sovrapposizione: {len(s1[first_index: ])}" # ritorno la lunghezza della sovrapposizione
                
                else: # in alternativa incremento gli indici
                    first_index -= 1
                    second_index += 1
                
                if abs(first_index) >= len(s1): # se il valore assoluto di first_index(rendendo quindi first_index positivo) raggiunge o supera il valore della lunghezza di s1 per evitare index errore si stabilisce che non si è trovata alcuna sovrapposizione
                    print("sovrapposizione non trovata")

                    return f"lunghezza di sovrapposizione {0}" # ritorno 0
    else:

        raise ValueError(f"una delle due sequenze di dna(o entrambe) non è valida, s1: {s1}, s2: {s2}")


def main(): # alcuni test

    t1 = individua_sovrapposizioni("TTGACCAGGTCA", "AACCGGTTAA")
    print(t1)

    t2 = individua_sovrapposizioni("GGTACCGTGA", "CGTGAACCTT")
    print(t2)

    t3 = individua_sovrapposizioni("AAGCTTACG", "ACGTTCGA")
    print(t3)

    t4 = individua_sovrapposizioni("TTACGAGTACGCTAGT", "ACGCTAGTCCGA")
    print(t4)

    t5 = individua_sovrapposizioni("AGCTAACG", "AACGTTCGA")
    print(t5)

    t6 = individua_sovrapposizioni("AAAA", "AAAA")
    print(t6)

    t7 = individua_sovrapposizioni("ACGT", "ATGC")
    print(t7)

main()
            
        
            

    
