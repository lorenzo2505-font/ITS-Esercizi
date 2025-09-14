class Frazione: # classe frazione

    def __init__(self, numeratore: int, denominatore: int): # attributi
        
        self.setNumeratore(numeratore)
        self.setDenominatore(denominatore)
    
    def setNumeratore(self, numeratore: int): # metodo set per il nome

        if type(numeratore) != int: # se il numeratore non è intero allora lo si imposta uguale a 13
            self.__numeratore = 13
        
        else:
            self.__numeratore = numeratore
    
    def setDenominatore(self, denominatore: int): # metodo set per il denominatore

        if type(denominatore) != int or denominatore == 0: # se il denominatore non è intero o è uguale a zero lo si imposta uguale a 5
            self.__denominatore = 5
        
        else:
            self.__denominatore = denominatore
    
    def getNumeratore(self) -> int: # metodo get per il numeratore

        return self.__numeratore
    
    def getDenominatore(self) -> int: # metodo get per il denominatore

        return self.__denominatore
    
    def value(self) -> float: # metodo value

        return round((self.__numeratore / self.__denominatore), 3) # ritorno il rapporto tra numeratore e denominatore approssimato di 3 cifre decimali
    
    def __str__(self) -> str: # metodo __str__
        
        return f"{self.__numeratore}/{self.__denominatore}"


def mcd(x: int, y: int) -> int: # funzione mcd: trova il massimo comun divisore tra due numeri

    x_list: list[int] = [i for i in range(1, x + 1) if x % i == 0] # lista contenente tutti i divisori di x
    y_list: list[int] = [j for j in range(1, y + 1) if y % j == 0] # lista contenente tutti i divisori di z
    
    return max(set(x_list).intersection(set(y_list))) # faccio il casting a set() delle due liste e ritorno il valore massimo dell'intersezione tra di loro

    # si usa l'intersezione tra i set perché ne restituisce uno con i valori comuni tra i due
    # questo perché Il Massimo Comune Divisore (MCD) è il più grande numero intero positivo che divide esattamente due o più numeri interi
    

def semplifica(fraction_list: list[Frazione]): # funzion semplifica per semplificare la frazione

    newlist: list[Frazione] = [] # definisco una nuova lista vuota

    for i in fraction_list: # itero la lista passata in input
        
        num = i.getNumeratore() # uso il metodo getNumeratore() per dare un valore alla variabile num
        den = i.getDenominatore() # uso il metodo getDenominatorte() per dare un valore alla variabile den
        div = mcd(num, den) # div è l'mcd tra numeratore e denominatore

        if div > 1: # se il valore dell'mcd è maggiore di 1 allora la frazione deve essrere semplificata

            num = num // div # divido il valore del numeratore per l'mcd
            den = den // div # divido il valore del denominatore per l'mcd

            i.setNumeratore(num) # reimposto il valore del numeratore 
            i.setDenominatore(den) # reimposto il valore del denominatore
        
        newlist.append(i) # aggiungo l'oggetto di classe Frazione alla nuova lista
    
    return newlist # ritorno la nuova lista

def fractionCompare(first_list: list[Frazione], second_list: list[Frazione]): # funzione che confronta i valori delle due liste di frazioni per dimostrare che sono uguali nonostante eventuali semplificazioni

    if len(first_list) != len(second_list):

        raise ValueError("le due liste non hanno la stessa lunghezza")
    
    for i in range(len(first_list)):

        print(f" Valore frazione originale: {first_list[i].value()} --- Valore frazione ridotta: {second_list[i].value()}")


def main():

    popa: Frazione = Frazione(2.5, 0)
    pierlions: Frazione = Frazione(1, 2)
    rossi: Frazione = Frazione(2, 4)
    colella: Frazione = Frazione(3, 5)
    pierre_damien: Frazione = Frazione(6, 9)
    nicholas: Frazione = Frazione(4, 7)
    marchetti: Frazione = Frazione(24, 36)
    acomanni: Frazione = Frazione(12, 36)
    boyko: Frazione = Frazione(40, 60)
    erald: Frazione = Frazione(5, 11)
    dioni: Frazione = Frazione(10, 45)
    bosco: Frazione = Frazione(42, 78)
    esposito: Frazione = Frazione(9, 15)

    l: list[Frazione] = [popa, pierlions, rossi, colella, pierre_damien, nicholas, marchetti, acomanni, boyko, erald, dioni, bosco, esposito]
    l_s: list[Frazione] = semplifica(l)

    fractionCompare(l, l_s)

main()
    

    
    