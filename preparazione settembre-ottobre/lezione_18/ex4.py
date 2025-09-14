'''Database di date: scrivere una classe che gestisca un database di date con il formato gg.mm.aaaa. 
È necessario implementare metodi per aggiungere una nuova data, 
eliminare una data specificata, 
modificarne una ed eseguire una query su una data specificata. 
Una query su una data specificata consente di recuperare una nuova data specificata. 
Si noti che una data è un oggetto per il database; deve essere istanziata da una stringa.'''

import re


class Data:

    def __init__(self, data: str):
        
        self.setData(data)
    
    def setData(self, data: str):
        
        if re.fullmatch(r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$", data):

            datesplit: list = data.split("/")

            if int(datesplit[0]) > 31:
                
                raise ValueError("non esistono mesi con più di 31 giorni")
            
            elif int(datesplit[1]) > 12:
                
                raise ValueError("i mesi non possono essere più di 12")
            
            elif int(datesplit[0]) > 28 and int(datesplit[1]) == 2:

                raise ValueError("febbraio non ha più di 28 giorni")
            
            elif int(datesplit[0]) > 30 and (datesplit[1] == 4 or datesplit[1] == 6 or datesplit[1] == 9 or datesplit[1] == 11):

                raise ValueError("aprile, giugno, settembre e novembre non possono avere più di 30 giorni")
            
            else:
                self.__data = data
        
        else:

            raise ValueError("la data non è scritta nel formato corretto")
    
    def getData(self) -> str:

        return self.__data



class DatabaseDates:

    def __init__(self):
        
        self.dates: list[Data] = []
    
    def aggiungi_data(self, data: Data):

        if data in self.dates:

            raise ValueError("la data è già presente nel database")
        
        self.dates.append(data)
    
    def elimina_data(self, data: Data):

        if data not in self.dates:

            raise ValueError("la data non è presente nel database")
        
        self.dates.remove(data)
    
    def modifica_data(self, data: Data, new_data: str):

        if data not in self.dates:

            raise ValueError("la data non è presente nel database")
        
        data.setData(new_data)
    
    def query_data(self, data: Data):

        if data not in self.dates:

            raise ValueError("la data non è presente nel database")
        
        return data.getData()
    
        
        



def main():

    lorenzo: Data = Data("25/03/2005")
    print(lorenzo.getData())

    popa: Data = Data("31/07/2025")
    print(popa.getData())

    popabase: DatabaseDates = DatabaseDates()
    popabase.aggiungi_data(lorenzo)
    popabase.aggiungi_data(popa)
    popabase.elimina_data(lorenzo)
    popabase.modifica_data(popa, "01/01/2004")
    print(popabase.query_data(popa))



main()
            

        