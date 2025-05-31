'''Crea una classe chiamata MathOperations per raggruppare alcune funzionalità aritmetiche di base. All'interno di questa classe, 
definisci due metodi statici:

add, che accetta due parametri numerici e ne restituisce la somma.

multiply, che accetta anch'esso due parametri numerici e ne restituisce il prodotto.

Infine, scrivi un piccolo programma driver per testare la funzionalità dei metodi add e multiply.
 Questo dovrebbe comportare la chiamata di entrambi i metodi con input di esempio
   e la stampa dei risultati per verificarne il corretto funzionamento.'''




class MathOperations:

    @staticmethod

    def add (n1: int, n2: int) -> int:

        somma = n1 + n2

        return somma
    
    @staticmethod


    def multiply(n1: int, n2: int) -> int:

        moltiplicazione = n1 * n2

        return moltiplicazione




m: MathOperations = MathOperations ()



print(m.add(1, 2))

print(m.multiply(3, 4))





