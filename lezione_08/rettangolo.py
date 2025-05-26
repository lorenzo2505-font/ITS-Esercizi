from classi_astratte import FormaGenerica

class Rettangolo(FormaGenerica):

    def __init__(self):
        

        super().__init__()

        self.setShape("rettangolo")
    
    def draw(self):
        print(f"\n{self.getShape()}\n")

        #istruzione per disegnare un rettangolo 5X10

        #outer for
        for i in range(5):
            #inner for
            for j in range(5 * 2):

                #lato a e lato b del triangolo

                if i == 0 or i == 5 - 1:
                    print("*", end = " ")
                
                #lato c e lato d del triangolo

                elif j == 0 or j == (5 * 2) - 1:
                    print("*", end = " ")
                
                #stampare spazio bianco 

                else:
                    print(" ", end = " ")
                
            print("\n", end = "")


        

        

