'''
 
Mostri Contro Alieni
 
 
Scrivere queste classi all'interno di un file chiamato ReP3_inizialeNome_Cognome. Ad esempio Mario Rossi 
dovrà scrivere queste classi all'interno del file chiamato ReP3_M_Rossi.
 
ATTENZIONE! Non saranno valutati programmi che generano errori in fase di esecuzione. Si consiglia pertanto
di “mettere sotto commento” le parti di programma che danno errori, in modo da permettere l'esecuzione del resto del programma. 

Definire le seguenti classi con attributi privati:

Creatura con le seguenti proprietà:
- attributi: nome (di tipo stringa, per indicare il nome della creatura)
- metodi: tutti i metodi standard, ovvero __init__, setter, getter e __str__
In particolare:

    il metodo setNome() deve fare un controllo se il nome inserito sia una stringa valida. 
    In caso contrario, impostare il nome della creatura con il valore di "Creatura Generica".

    il metodo __str__ deve mostrare in output: "Creatura: nome creatura"



Alieno (che eredita da Creatura) con le seguenti proprietà:
- attributi: matricola (di tipo intero positivo), munizioni (una lista di 15 interi positivi)
- metodi: setter, getter, __str__
In particolare:

    il metodo setMatricola() (privato), non riceve argomenti in input e deve inizializzare l'attributo matricola con un numero intero positivo casuale tra 10000 e 90000.

Per generare un numero intero casuale nell'intervallo [a, b] (ovvero estremi inclusi), importare il modulo random e usare la funzione randint(a,b) del modulo;
 

    il metodo setMunizioni() (privato) non riceve argomenti in input e deve inizializzare l'attributo munizioni con una lista di 15 numeri interi positivi i cui elementi sono numeri della sequenza 0, 1, 4, 9, 16, 25, 36, 49, ... Usare le list comprehension.

    il metodo __init__ deve inizializzare la superclasse, inizializzare la matricola e le munizioni.

Inoltre, i nomi di tutti gli alieni devono essere "Robot-" + matricola (ad esempio, "Robot-16326", scritto con la R maiuscola).
Pertanto, nel metodo __init__ impostare il nome dell'Alieno come richiesto, effettuando opportuni controlli. Nel caso in cui il nome dell'alieno non sia conforme, mostrare il seguente messaggio e re-impostare il nome in modo corretto: "Attenzione! Tutti gli Alieni devono avere il nome "Robot" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!".

    il metodo __str__ deve mostrare in output: "Alieno: nome alieno" (ad esempio: Alieno: Robot-16326)


Mostro ( che eredita da Creatura) con le seguenti proprietà:
- attributi: urlo_vittoria (di tipo stringa), gemito_sconfitta (di tipo stringa), assalto (una lista di 15 interi positivi)
- metodi: setter, getter, __str__
In particolare:

    il metodo __init__ deve ricevere il nome del mostro, il suo urlo della vittoria ed il suo gemito sconfitta. Inoltre, deve inizializzare assalto.

    il metodo setAssalto() (privato) non riceve argomenti in input e deve inizializzare l'attributo assalto con 
    una lista di 15 numeri interi positivi casuali tra 1 e 100, estremi inclusi, 
    tutti diversi tra loro.

    i metodi setVittoria(vittoria: str) e setSconfitta(sconfitta: str) (privati), devono controllare se i valori di vittoria e sconfitta siano valori validi. 
    In caso contrario, devono impostare gli attributi urlo_vittoria a "GRAAAHHH" e gemito sconfitta a "Uuurghhh".

    ad esempio, se il nome del mostro è "Godzilla", il metodo __str__ dovrà mostrare a schermo: 
    Mostro: gOdZiLlA, ovvero il nome del mostro scritto con i caratteri alternati minuscolo-maiuscolo.



All'interno del file ReP3_inizialeNome_Cognome (fuori dalla classi) definire le seguenti funzioni:

    pariUguali(a: list[int], b: list[int]). Questo metodo riceve in input due liste a e b di interi positivi e deve restituire una lista c.

Ogni elementi della lista c deve essere uguale a:
- 1 se l'elemento i-esimo di a e l'elemento i-esimo di b sono sono entrambi pari
- 0 altrimenti

    combattimento(a: Alieno, m: Mostro). Questo metodo riceve in input un oggetto della classe Alieno ed un oggetto della classe Mostro.
      Il metodo deve controllare la validità di a e la validità di m. Se a non è un Alieno o se m non è un Mostro, 
      il combattimento deve essere interrotto, mostrare un opportuno messaggio e ritornare None. Altrimenti, 
      se a e m sono oggetti validi, il metodo deve simulare il combattimento tra Mostro e Alieno, restituendo la creatura vincitrice. 
      Il combattimento consiste nell'applicare la funzione pariUguali() alle munizioni dell'Alieno e all'assalto del Mostro. 
      Se la lista prodotta in output dal pariUguali() ha più di 4 elementi con valore 1, allora il vincitore è il mostro. Altrimenti, 
      il vincitore è l'alieno. Se vince il mostro, sullo schermo viene stampato per 3 volte l'urlo della vittoria, 
      altrimenti viene stampato il gemito della sconfitta.


    proclamaVincitore(c: Creatura). Questo metodo stampa a schermo se hanno vinto gli alieni o i mostri ( a seconda dell'oggetto c) e , 
    mostra il vincitore all'interno di un rettangolo con contorno di * come nell'esempio.


*****************************

*                                         *

*    Alieno: Robot-25855    *

*                                         *

*****************************

*************************

*                                   *

*    Mostro: gOrThOr    *

*                                    *

*************************

Suggerimento: stampare prima il rettangolo vuoto, le cui dimensioni sono altezza 5 e lunghezza = lunghezza di c.__str__() + 10
poi, modificare il codice in questo modo:
quando si arriva alla riga centrale del rettangolo (ovvero i=2), si deve stampare il nome del vincitore al centro del rettangolo.
per far questo si deve imporre la condizione i=2 e j =5. Se la condizione è verificata, stampare la creatura c (print(c), end=""), stampare 5 spazi vuoti e un * (print(     *), end="") e poi interrompere l'iterazione corrente.


Infine,

    Scrivere nel metodo main, un codice Python che

- Inizializza un mostro e un alieno e stampa i dati corrispondenti sullo schermo.
- Esegue un combattimento tra i due oggetti creati.
- Proclama il vincitore.'''



import random


class Creatura:

    def __init__(self, nome: str):

        self.setNome(nome)
    
    def setNome(self, nome: str):

        if nome:

            self._nome = nome
        
        else:

            self._nome = "Creatura Generica"
    
    def getNome(self):

        return self._nome
    
    def __str__(self):
        
        return f"nome creatura: {self._nome}"



class Alieno(Creatura):


    def __init__(self, nome: str):
        super().__init__(nome)

        self._setMatricola()
        self._setMunizioni()

        self.setNome(nome)
    

    def _setMatricola(self):


        n: int = random.randint(10000, 90000)

        self._matricola = n
    
    def _setMunizioni(self):

        munizioni: list[int] = [i ** 2 for i in range(0, 15)]

        self._munizioni = munizioni
    
    def setNome(self, nome: str):

        if nome != f"Robot-{self._matricola}":

            print("Attenzione! Tutti gli Alieni devono avere il nome Robot seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")

            self._nome = f"Robot-{self._matricola}"
        
        else:

            self._nome = nome
    

    def getMatricola(self):

        return self._matricola
    
    def getMunizioni(self):

        return self._munizioni
    
    def getNome(self):
        return super().getNome()
    
    def __str__(self):
        return f"Alieno: {self._nome}"
    


class Mostro(Creatura):

    def __init__(self, nome: str, urlo_vittoria: str, gemito_sconfitta: str):
        super().__init__(nome)

        self._setVittoria(urlo_vittoria)

        self._setSconfitta(gemito_sconfitta)

        self._setAssalto()
    
    def _setVittoria(self, urlo_vittoria: str):

        if urlo_vittoria != "GRAAAHHH":

            self._vittoria = "GRAAAHHH"
        
        else:

            self._vittoria = urlo_vittoria
    
    def _setSconfitta(self, gemito_sconfitta: str):

        if gemito_sconfitta != "Uuurghhh":

            self._sconfitta = "Uuurghhh"
        
        else:

            self._sconfitta = gemito_sconfitta
    
    def _setAssalto(self):

        pass
    
    

        
