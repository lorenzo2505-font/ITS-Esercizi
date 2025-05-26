'''text analisis: Crea una funzione che prenda un paragrafo e conti il ​​numero di occorrenze di ogni parola.

La funzione dovrebbe stampare un report che mostri le parole più frequenti e il loro numero di occorrenze.

Puoi usare un ciclo for per scorrere le parole nel testo e un dizionario per memorizzare le occorrenze.'''


def text_analisis (plist: list[str] ):

    vuoto: str = ""

    mydict: dict = {}

    for i in range(len(plist)):

        vuoto = vuoto + f" {plist[i]}"
    

    for i in range(len(plist)):

        mydict[plist[i]] = plist.count(plist[i])

    
    return vuoto, mydict



t = text_analisis (["spectacular", "spectacular", "spider-man"])

print(t)








   



   

 












