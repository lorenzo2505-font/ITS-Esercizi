from __future__ import annotations
import random
import time


def posizioni(t: int, l: int): # funzione per gestire le posizioni di lepre e tartaruga
    percorso: list = [] # inizializzo la lista del percorso come una lista vuota
    

    for i in range(70): # aggiungo le 70 posizioni a percorso
        i = "_"
        percorso.append(i)
    
    if t >= 70 and l >= 70: # se entrambi gli animali hanno raggiunto il traguardo allora è un pareggio e dovrò mettere pari alla posizione 70 e proclamare il pareggio
        percorso[t - 1] = "PARI"
        print(*percorso)
        print("PAREGGIO!")
    
    elif t == l: # se entrambi gli animali hanno la stessa posizione, la lepre morde la tartaruga, verrà stampato ouch
        percorso[t -1] = "OUCH"
        print(*percorso)
        
    
    elif t >= 70: # se la tartaruga raggiunge il traguardo mostro le posizioni dei due animali proclamando la tartaruga come vincitore
        percorso[t - 1] = "T" 
        percorso[l - 1] = "L"
        print(*percorso)
        print("VINCE LA TARTARUGA!")
    
    elif l >= 70: # se la lepre raggiunge il traguardo mostro le posizioni dei due animali proclamando la lepre come vincitore
        percorso[t - 1] = "T" 
        percorso[l - 1] = "L"
        print(*percorso)
        print("VINCE LA LEPRE!")
    
    else: # se non si verifica nessuna delle 4 condizioni precedenti mostro semplicemente le posizioni dei due animali
        percorso[t - 1] = "T" 
        percorso[l - 1] = "L"
        print(*percorso)

def mosse_tartaruga(t: int, energia_totale: int): # funzione in cui gestisco le mosse della tartaruga
    p = random.randint(1, 10) # uso random per far muovere casualmente la tartaruga
    # metto un indicatore di energia, ad ogni mossa che fa la tartaruga, vi è un costo di energia, se l'energia totale non rientra nel costo quet'ultima viene aumentata di 10
    ostacoli: dict = {15: -3, 30: -5, 45: -7}
    bonus: dict = {10: 5, 25: 3, 50: 10}

    if 1 <= p <= 5: # propabilità 50% avanza di 3
        costo_energia = 5

        if costo_energia > energia_totale:
            energia_totale += 10
        
        energia_totale -= costo_energia
        t += 3
    
    elif 6 <= p <= 7: # probabilità 20% scende di 6
        costo_energia = 10

        if costo_energia > energia_totale:
            energia_totale += 10
        
        energia_totale -= costo_energia
        t -= 6

        if t < 1: # se la posizione della tartaruga va sotto l'1 la reimposto a 1
            costo_energia = 3
            
            if costo_energia > energia_totale:
                energia_totale += 10
            
            energia_totale -= costo_energia

            t = 1
    
    else: # probabilità 30% avanza di 1
        t += 1
    
    if t > 70:
        t = 70 # se la posizione della tartaruga va oltre il 70 la reimposto a 70
    
    if energia_totale < 0:
        energia_totale = 0
    
    if t in ostacoli:
        t += ostacoli[t]
    
    if t in bonus:
        t += bonus[t]

    return t, energia_totale # ritorno il valore della posizione della tartaruga utile poi nella gestione delle posizioni

def mosse_lepre(l: int, energia_totale: int): # funzione in cui gestisco le mosse della lepre 
    p = random.randint(1, 10) # uso random per far muovere casualmente la lepre
    ostacoli: dict = {15: -3, 30: -5, 45: -7}
    bonus: dict = {10: 5, 25: 3, 50: 10}
    

    if 1 <= p <= 2: # 20% non fa niente
        energia_totale += 10
        
        if energia_totale > 100:
            energia_totale = 100

        pass

    elif 3 <= p <= 4: # 20% avanza di 9
        costo_energia = 15

        if costo_energia > energia_totale:
            pass

        else:
            energia_totale -= costo_energia
            l += 9
    
    elif p == 5: # 10% scende di 12
        costo_energia = 20
        energia_totale -= costo_energia
        l -= 12

        if l < 1: # se la posizione della lepre va sotto l'1 la reimposto a 1
            l = 1
    
    elif 6 <= p <= 8: # 30% avanza di 1
        costo_energia = 5
        energia_totale -= costo_energia
        l += 1
    
    else: # probabiltà 20 % scende di 2 
        costo_energia = 8
        energia_totale -= costo_energia
        l -= 2

        if l < 1: # se la posizione della lepre va sotto l'1 la reimposto a 1
            l = 1
    
    if l > 70: # se la posizione della lepre va oltre il 70 la reimposto a 70
        l = 70
    
    if energia_totale < 0:
        energia_totale = 0
    
    if l in ostacoli:
        l += ostacoli[l]
    
    if l in bonus:
        l += bonus[l]
    

    return l, energia_totale # ritorno il valore della posizione della lepre utile poi nella gestione delle posizioni

t = 1
energy_t = 100

# nel main inizializzo la posizione dei due animali a 1

l = 1
energy_l = 100

condizioni_meteo: list = ["sole", "pioggia"] # possibili condizioni meteo

while True: # ciclo infinito
    #time.sleep(1) # imposto la funzione time perché gli animali fanno le loro mosse a ogni ticchettio dell'orologio
    meteo = random.choice(condizioni_meteo) # ad ogni ticchettio dell'orologio viene scelta casualmente una condizione meteo

    
    
    t, energy_t = mosse_tartaruga(t, energy_t) # richiamo la funzione mosse_tartaruga per cambiare la sua posizione
    l, energy_l = mosse_lepre(l, energy_l)  # richiamo la funzione mosse_lepre per cambiare la sua posizione

    if meteo == "pioggia": # se meteo è uguale a pioggia la posizione della tartaruga scende di 1 mentre quella della lepre scende di 2
        t -= 1
        l -= 2

    posizioni(t, l) # richiamo la funzione posizione che mostrerà le posizioni aggiornate degli animali

    if t >= 70 or l >= 70: # il ciclio si interrompi quando almeno uno dei due animali raggiunge il traguardo 
        break









