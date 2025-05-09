def alpha ():
    print("executing alpha")

def beta ():
    alpha ()
    print("executing beta")

def gamma ():
    print("executing gamma")
    beta ()

gamma()


'''
ordine chiamata:
gamma() -> beta()  -> alpha()

ordine rimozione

alpha() -> beta() -> gamma()

output
executing gamma
executing alpha
executing beta'''