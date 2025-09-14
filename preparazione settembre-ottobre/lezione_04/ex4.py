'''4. Analisi del testo:

Crea una funzione che prenda un paragrafo e conti il numero di occorrenze di ogni parola.
La funzione dovrebbe stampare un report che mostri le parole più frequenti e il loro numero di occorrenze.
Puoi usare un ciclo for per scorrere le parole nel testo e un dizionario per memorizzare le occorrenze.'''



def analisiTestuale(testo: str):

    mydict: dict = {}

    for i in testo.split(" "):

        if i not in mydict:
            mydict[i] = 1
        
        else:
            mydict[i] += 1
    
    print(mydict)


analisiTestuale("apelle figlio di apollo fece una palla di pelle di pollo")
