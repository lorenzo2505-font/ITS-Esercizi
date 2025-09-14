'''8. Simulatore di bancomat:

Creare una funzione che simula un bancomat.

Inizializzare un conto con un saldo iniziale.

Consentire all'utente di effettuare transazioni come depositi, prelievi e controlli del saldo.

Convalidare le transazioni in base al saldo del conto e ai fondi disponibili.

Fornire un feedback appropriato all'utente per ogni transazione.'''


def bancomat(saldo_iniziale: float, deposito: bool = False, prelievo: bool = False, controllo_saldo = False):

    fondi_disponibili: float = 1000000

    if deposito:
        d: float = float(input("quanto vuoi depositare ?: "))

        if saldo_iniziale < d:
            
            raise ValueError("conto insufficiente")
        
        saldo_iniziale -= d
        fondi_disponibili += d
        
        print(f"hai depositato {d}$, ora hai {saldo_iniziale}$")
    
    if prelievo:
        p: float = float(input("quanto vuoi prelevare ?: "))

        if fondi_disponibili < p:

            raise ValueError("siamo spiacenti ma non abbiamo abbastanza fondi")
        
        fondi_disponibili -= p
        saldo_iniziale += p

        print(f"prelevato {p}$, ora hai {saldo_iniziale}")
    
    if controllo_saldo:
        
        print(f"saldo attuale: {saldo_iniziale}$")



bancomat(500.0, deposito = True, prelievo = True, controllo_saldo = True)
        

    