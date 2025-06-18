
   




class Frazione:

    def __init__(self, numeratore: int, denominatore: int):


        self.setNumeratore(numeratore)

        self.setDenominatore(denominatore)
    

    def setNumeratore(self, numeratore):

        if type(numeratore) == int:

            self._numeratore = numeratore
        
        else:

            self._numeratore = 13
    

    def setDenominatore(self, denominatore: int):


        if denominatore == 0 or type(denominatore) != int:

            self._denominatore = 5
        
        else:

            self._denominatore = denominatore
    

    def getNumeratore(self):

        return self._numeratore
    
    def getDenominatore(self):

        return self._denominatore
    

    def value(self):

        return round(self._numeratore / self._denominatore, 3)

    def __str__(self):
        

        return f"{self._numeratore}/{self._denominatore}"
    
    def __repr__(self):

        return f"{self._numeratore}/{self._denominatore}"
         
    








def mcd(x: int, y: int):

    divisori_x: list[int] = []

    divisori_y: list[int] = []


    for i in range(1, x + 1):

        if x % i == 0:

            divisori_x.append(i)
    

    for i in range(1, y + 1):

        if y % i == 0:

            divisori_y.append(i)
    
    
    while True:

        if x > y:

            if max(divisori_y) in divisori_x:

                return max(divisori_y)
            
            else:

                divisori_y.remove(max(divisori_y))
        

        elif x < y:


            if max(divisori_x) in divisori_y:

                return max(divisori_x)
            
            else:

                divisori_x.remove(max(divisori_x))
        
        else:

            return max(divisori_x)
        
        if (len(divisori_x) == 1) or (len(divisori_y) == 1):

            return 1









def semplifica(mylist: list[Frazione]) -> list[Frazione]:

    newlist: list[Frazione] = []

    


    for i in mylist:

        t = mcd(i.getNumeratore(), i.getDenominatore())

        if t == 1:

            newlist.append(i)
        
        else:

            n = i.getNumeratore()

            d = i.getDenominatore()

            

            while t != 1:

                n //=t

                d //=t

                t = mcd(n, d)
            
            i.setNumeratore(n)

            i.setDenominatore(d)
            
            newlist.append(i)
    
    return newlist








def fractionCompare(original_list:list[Frazione], s_list: list[Frazione]) :


    for i in range(len(original_list)):

        print(f"valore frazione originale: {original_list[i].value()}, valore frazione semplificata: {s_list[i].value()}")

        



#fractionCompare(lista, prova)



f1: Frazione = Frazione(2.5, 0)


f2: Frazione = Frazione(1, 2)

f3: Frazione = Frazione (2, 4)

f4: Frazione = Frazione(3, 5)

f5: Frazione = Frazione(6, 9)

f6: Frazione = Frazione(4, 7)

f7: Frazione = Frazione(24, 36)

f8: Frazione = Frazione(12, 36)

f9: Frazione = Frazione(40, 60)

f10: Frazione = Frazione(5, 11)

f11: Frazione = Frazione(10, 45)

f12: Frazione = Frazione(42, 78)

f13: Frazione = Frazione(9, 15)


frazioni: list[Frazione] = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13]


semplifica_frazioni = semplifica(frazioni)

print(semplifica_frazioni)

comparazione = fractionCompare(frazioni, semplifica_frazioni)













    


    
    
        





        