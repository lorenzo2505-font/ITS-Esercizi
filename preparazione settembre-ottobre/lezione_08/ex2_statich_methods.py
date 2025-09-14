'''Crea una classe chiamata MathOperations per raggruppare alcune funzionalità aritmetiche di base.
All'interno di questa classe, definisci due metodi statici:

add, che accetta due parametri numerici e ne restituisce la somma.

multiply, che accetta anch'esso due parametri numerici e ne restituisce il prodotto.

Infine, scrivi un piccolo programma driver per testare la funzionalità dei metodi add e multiply.
Questo dovrebbe comportare la chiamata di entrambi i metodi con input di esempio
e la stampa dei risultati per verificarne il corretto funzionamento.'''


class MathOperations:

    @staticmethod

    def add(p1: int, p2: int):
        
        return p1 + p2
    
    @staticmethod

    def multiply(p1: int, p2: int):

        return p1 * p2


m: MathOperations = MathOperations()

print(m.add(1, 2))

print(m.multiply(5, 4))


