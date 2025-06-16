'''

8.A Si Scriva in Python in un file frazioni.py una classe Frazione, i cui attributi privati siano rispettivamente numeratore e denominatore.
Si definiscano i metodi __init__, setter, getter, __str__, value.
In particolare:

    il metodo value(), deve restituire il valore della frazione, ovvero numeratore / denominatore arrotondato a 3 cifre decimali;

    il metodo __str__ deve mostare in output la frazione nel seguente modo: "numeratore / denominatore ";

    i metodi setter devono controllare che il valore inserito sia un intero, 

    in caso contrario il numeratore ed il denominatore devono essere impostati per default rispettivamente a 13 e 5. 

    Inoltre, il metodo setter relativo al denominatore deve assicurarsi che questo non sia mai uguale a 0. 

    Nel caso in cui il denominatore passato sia 0, impostarlo per default a 5.

Suggerimento: per verificare che il numeratore ed il denominatore siano numeri interi, usare la funzione is_integer().'''




'''8.B Il Massimo Comun Divisore di due o più numeri è il più grande divisore comune dei numeri considerati.
Ad esempio, se consideriamo i numeri 12 e 18, il loro Massimo Comun Divisore è mcd(12,18) = 6.
Infatti,

    i divisori di 12 sono:

        12 = 1, 2, 3, 4, 6, 12

    i divisori di 18 sono:

        18 = 1, 2, 3, 6, 9, 18
        
        


il divisore più grande che 12 e 18 hanno in comune è 6.

Scrivere nel file frazione.py una funzione  mcd(int x, int y) per il calcolo del Massimo Comune Divisore.
 
Nel caso in cui esista un Massimo Comun Divisore tra i numeri x e y, allora la funzione deve ritornarlo come numero intero.
Altrimenti, nel caso in cui non esista un massimo Comun Divisore tra i numeri x e y, la funzione deve ritornare 1.
   

Suggerimento: per semplicità, per implementare la funzione richiesta, 
trovare una soluzione che generalizzi l'esempio proposto e che tenga conto dei casi x > y e x < y per evitare di replicare righe di codice.'''



'''8.C Una frazione si dice irriducibile se il numeratore e il denominatore non hanno divisori comuni, 

ovvero il più grande divisore comune tra numeratore e denominatore è 1.

Sia l una lista di frazioni, ovvero una lista di oggetti della classe Frazione.

Si scriva nel file frazioni.py una funzione chiamata semplifica() che data in input una lista di frazioni ritorni in output una lista di frazioni irriducibili.
 
Nello specifico:

    se una frazione f della lista data in input è già irriducibile, allora inserire questa frazione f nella lista da ritornare in output.

 

    se una frazione f della lista data in input può essere semplificata, in una frazione irriducibile f1, allora si deve prima semplicare la frazione f, 
    ottenendo la frazione irriducibile f1 e poi inserire f1 nella lista da ritornare in output.


Suggerimento: Leggere bene la traccia dell'intero esercizio per capire come implementare la funzione semplifica.
Inserire in modo adeguato le seguenti frazioni nella lista l.'''



'''8.D Scrivere in Python una funzione chiamata fractionCompare() che prende in input la lista di frazioni l originale e la lista con le frazioni di l semplificata.
 
Usando il metodo value(), dimostrare che il valore di ogni funzione di entrambe le liste non cambia, stampandolo in output.
Esempio:

    Valore frazione originale: 0.538 --- Valore frazione ridotta: 0.538'''
   




class Frazione:

    def __init__(self, numeratore: int, denominatore: int):


        self.setNumeratore(numeratore)

        self.setDenominatore(denominatore)
    

    def setNumeratore(self, numeratore):

        if numeratore % 1 == 0:

            self._numeratore = numeratore
        
        else:

            self._numeratore = 13
    

    def setDenominatore(self, denominatore: int):


        if denominatore % 1 == 0:

            self._denominatore = denominatore
        
        elif (denominatore == 0) or (denominatore % 1 != 0):

            self._denominatore = 5
    

    def getNumeratore(self):

        return self._numeratore
    
    def getDenominatore(self):

        return self._denominatore
    

    def value(self):

        return round(self._numeratore / self._denominatore, 3)

    def __str__(self):
        

        return f"{self._numeratore}/{self._denominatore}"
    
    def __repr__(self):

        return f"{self._numeratore}/{self._denominatore}"
         
    



f: Frazione = Frazione(10, 9)


#print(f.value())

#print(f)




def mcd(x: int, y: int):

    divisori_x: list[int] = []

    divisori_y: list[int] = []


    for i in range(1, x + 1):

        if x % i == 0:

            divisori_x.append(i)
    

    for i in range(1, y + 1):

        if y % i == 0:

            divisori_y.append(i)
    
    
    while True:

        if x > y:

            if max(divisori_y) in divisori_x:

                return max(divisori_y)
            
            else:

                divisori_y.remove(max(divisori_y))
        

        elif x < y:


            if max(divisori_x) in divisori_y:

                return max(divisori_x)
            
            else:

                divisori_x.remove(max(divisori_x))
        
        else:

            return max(divisori_x)
        
        if (len(divisori_x) == 1) or (len(divisori_y) == 1):

            return 1





test = mcd(12, 18)


#print(test)



def semplifica(mylist: list[Frazione]) -> list[Frazione]:

    newlist: list[Frazione] = []

    


    for i in mylist:

        t = mcd(i.getNumeratore(), i.getDenominatore())

        if t == 1:

            newlist.append(i)
        
        else:

            n = i.getNumeratore()

            d = i.getDenominatore()

            while mcd(n, d) != 1:

                n //=mcd(n, d)

                d //=mcd(n, d)
            
            i.setNumeratore(n)

            i.setDenominatore(d)
            
            newlist.append(i)
    
    return newlist




marco: Frazione = Frazione(6, 4)

matteo: Frazione = Frazione(10, 5)



lista: list[Frazione]= [marco, matteo]



prova = semplifica(lista)

print(prova)



def fractionCompare(original_list:list[Frazione], s_list: list[Frazione]):
    pass

    
        





        