#definire funzione 

'''def nome_funzione (lista di parametri):
     istruzioni per la struttura della funzione'''


'''def function_name  (a: int, b: int): #si scrive def per segnalare all'interprete che si sta definendo la funzione, invece i parametri fanno da input per la funzione
     #codice che deve essere eseguito 
    result: int = 0
    for  i in range (a, b+1):            #struttura funzione, qui vi è il codice che la funzione eseguirà
            risultato = risultato + i 
    return risultato 
    '''
#questo spazio di indentazione è importante, scriviamo fuori dalla struttura di  funzione

 #soluzione di un esercizio

def sum_in_range (a: int, b:  int):
    #definisce la funzione
    result: int = 0
    #calcolo  somma
    for i in range(a, b  + 1):
        result = result + i
    #restituisce il  valore della somma come  output della  funzione sum
    return  result

#uso della funzione per calcolare la sommma di interi  da 1 a 20 

print(f"la somma da 1  a 20 è {sum_in_range(1, 20)}")

#uso della funzione per calcolare gli interi da 20  a 37

print(f"la somma da 20 a 37 è {sum_in_range(20, 37)}")

#usa la funzione sum_in_range per  calcolare una somma di interi da 35 a 49

print(f"la somma da 35 a 49  è {sum_in_range(35, 49)}")
 
       