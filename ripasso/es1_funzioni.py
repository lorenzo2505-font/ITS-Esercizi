'''Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è
soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X
è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa"
oppure "Azione negata" a seconda delle condizioni che sono soddisfatte.'''


def fun(x: bool, y: bool, z: bool) -> str:


    if x == True and (y == True or z == True):

        return "azione permessa"
    
    else:

        return "azione negata"



t = fun(True, True, False)

print(t)



