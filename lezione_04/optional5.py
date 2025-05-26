'''5. Inventory Management System:

    Create a list to store the items in inventory.

    Create a function that defines an item with a code, name, quantity, and price.

    Implement functions to add, remove, search, and update items in the inventory.

    Use for loops to manage the various inventory operations.

'''

import random

inventario: list = ["spada", "piccone", "pala", "zappa", "banco"]


def defying_items():

    
    deflist: list[dict] = []

    


    for i in range(len(inventario)):

        deflist.append({"code": hash(inventario[i]), "name": inventario[i], "quantity": random.randint(1, 10), "price": random.randint(1, 10) })
    
    d = deflist

    
    return d




def custom_items ():

    a = defying_items()

    questions: int = int(input("quante operazioni vuoi fare ?: "))

    options: list = ["add", "remove", "search"]

    for nq in range(questions):

        option = input("che vuoi fare ?: ")

        if option not in options:

            raise Exception("this option is not in our list")
        
        if option == "add":

            

            new_item: str = str(input("nome del nuovo item: "))

            a.append({"code": hash(new_item), "name": new_item, "quantity": random.randint(1, 10), "price": random.randint(1, 10)})

            print("confermata l'aggiunta")

        
        if option == "remove":
                
                n: int = int(input("inserisci indice: "))

                for i in range(len(a)):

                    if i == n:

                        a.pop(i)

                        print("confermata la rimozione")
                    
                    else:

                        pass
                
                        

            

                        
                            
                        
                       

        
        if option == "search":

            search_with_n: int = int(input("inserisci indice: "))

            for i in range(len(a)):

                if i == search_with_n:

                    print(a[i])
                
                else:
                    pass

                

                       



custom_items ()
                    

                       


                        
                 

                    



                



            


        







        

