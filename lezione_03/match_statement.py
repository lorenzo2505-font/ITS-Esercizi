#come funziona il match statement

'''
match variable:
    case variable  value 1:
        instructions for variable_value1
    case variable_value2:
         instructions for variable_value2
    case_:
     instruction for default case
       '''

#inserimento di un numero:
n = int(input("inserisci posizione: ")) #controlla l'inserimento di un numero, dato che deve restituire la forma cardinale

#match statement 
match n:
    #n = 1
    case 1:
        print(f"{n}st!")
    #n = 2
    case 2:
        print(f"{n}nd!")
    #n = 3
    case 3:
        print(f"{n}rd!")
    #default case
    case _ :
        print(f"{n}th!")

