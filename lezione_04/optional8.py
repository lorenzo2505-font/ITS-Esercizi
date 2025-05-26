'''Simulatore di bancomat:

Crea una funzione che simula un bancomat.

Inizializza un conto con un saldo iniziale.

Consente all'utente di eseguire transazioni come depositi, prelievi e controlli del saldo.

Convalida le transazioni in base al saldo del conto e ai fondi disponibili.

Fornisce un feedback appropriato all'utente per ogni transazione.'''



#versione mia iniziale



def bancomat(conto: float) -> float:


    fondi: float = 500000000.0

    


    options: list = ["deposito", "prelievo", "controllo del saldo"]

    option = input("inserisci opzione: ")

    if option not in options:

        return f"errore, il programma si fermerà"
    
    else:

        if option == "deposito":

            quantità: float = float(input("quanto vuoi depositare ?: "))

            conto += quantità


            return f"transazione approvata, soldi depositati: {quantità} euro, conto: {conto}, euro"
        
        
        
        if option == "prelievo":

            p: float = float(input("quanto devi prelevare ?: "))

            if p < conto and p < fondi:

                conto -= p

                return f"transazione approvata, hai prelevato: {p} euro, conto: {conto} euro"
            
            elif p >= fondi:

                return "siamo spiacenti, non abbiamo fondi, transazione non eseguibile"
            
            elif p > conto:

                return f"transazione non eseguibile, il conto non è sufficiente, hai chiesto: {p} euro, il tuo conto è di {conto} euro"

               
        
        if option == "controllo del saldo":

            return f"conto: {conto} euro"
        








#seconda versione dopo check soluzioni prof


def bancomat2(conto: float):


    

    


    options: list = ["deposito", "prelievo", "controllo del saldo", "uscire"]

    while True:

        option = input(f"inserisci opzione tra: {options}: ")

        if option not in options:

            print(f"errore, riprova")
        
        else:

            if option == "deposito":

                quantità: float = float(input("quanto vuoi depositare ?: "))

                conto += quantità


                print(f"transazione approvata, soldi depositati: {quantità} euro, conto: {conto}, euro") 
            
            
            
            if option == "prelievo":

                p: float = float(input("quanto devi prelevare ?: "))

                if conto >= p:

                    conto -= p

                    print(f"transazione approvata, hai prelevato: {p} euro, conto: {conto} euro") 

                

                
            
            if option == "controllo del saldo":

                print(f"conto: {conto} euro") 
            
            if option == "uscire":
                break

    return f"ci auguriamo abbia usato il servizio nel modo migliore possibile"

                

                

                



t = bancomat2(500.0)

print(t)
        
    
            


            
            
          




