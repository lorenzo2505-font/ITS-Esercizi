lista = [x for x in range(1, 10 + 1)]

def fric(ll):

    # 1) bisogna mettere una condizione per elaborare il passo
    # 2) condizione di fine
    # una funzione ricorsiva può essere tradotta in maniera iterativa (for, while)

    print(ll)

    if len(ll) == 1:
        return
    
    else:
        
        a = ll[0]
        print(a)
        fric(ll[1:]) 

fric(lista)