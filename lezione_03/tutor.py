'''Progettare un algoritmo che assegni i 10 tutor disponibili agli studenti che necessitano di recupero in un istituto scolastico. 
Per ogni studente dato in input, il sistema deve controllare la disponibilità dei tutor e, nel caso di disponibilità, assegnarlo allo studente.
 Se il numero di tutor disponibili scende a zero, occorre aumentare il numero di studenti in lista d'attesa. 
 Occorre confermare sia l’assegnazione del tutor con successo che l'inserimento nella lista d’attesa allo studente.
   L'algoritmo termina solo quando il numero di tutor è pari a 0 e la lista d'attesa conta 50 studenti. '''

tutor = 10

studenti_in_attesa = 40

while studenti_in_attesa < 50:
    studente = str(input("inserisci il nome dello studente: "))
    
    
    if tutor > 0:
        print("tutor assegnato")
        tutor-=1
    else:
        studenti_in_attesa+=1
        print("studente inserito nella sala d'attesa")

