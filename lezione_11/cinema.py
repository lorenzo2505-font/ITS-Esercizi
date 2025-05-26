'''Sistema di Prenotazione Cinema

Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema.
 Il cinema ha diverse sale, ognuna con un diverso film in programmazione. 
 Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.

 
Classi:
- Film: Rappresenta un film con titolo e durata.
 
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.
Metodi:

    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.
Metodi:

    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.
Test case:
Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
Un cliente sceglie un film e prenota un certo numero di posti.
Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.'''


class Film:

    def __init__(self, titolo: str, durata: int):

        self.set_titolo(titolo)
        
        self.set_durata(durata)

        

    
    def set_titolo(self, titolo):

        if titolo:

            self.titolo = titolo

        else:

            raise Exception
        
    
    def get_titolo(self):

        return self.titolo
    

    def set_durata(self, durata: int):

        self.durata = f"{durata} minuti"
    
    def get_durata(self):
        
        return self.durata
    
    def __str__(self):

        return f"titolo: {self.titolo}, durata: {self.durata}"


f: Film = Film("il cavaliere oscuro", 152)

#print(f)
    
    





class Sala:

    def __init__(self, n: int, film: Film, posti_totali: int):

        


        self.set_n(n)

        self.set_film(film)

        self.set_posti_totali(posti_totali)

        

    def set_n(self, n: int):

        if n > 0:

            self.n = n

        else:

            raise ValueError("il numero deve essere maggiore di zero")
    
    def get_n(self):

        return self.n
    
    def set_film(self, film: Film):

        if film:

            self.film = film
    
    def get_film(self):

        return self.film
    
    def set_posti_totali(self, posti_totali: int):

        if posti_totali <= 0:

            raise ValueError("i posti non possono essere maggiori o uguali a zero")
        
        else:

            self.posti_totali = posti_totali
    
    def posti_disponibili(self):

        return self.posti_totali
    
    def prenota_posti(self, posti_prenotati: int):

        if self.posti_totali >= posti_prenotati:

            print("prenotazione avvenuta con successo")

            self.posti_totali -= posti_prenotati

            self.posti_prenotati = posti_prenotati

        else:

            raise Exception("non vi sono abbastanza posti")
    
    def get_prenotati(self):

        return self.posti_prenotati
    
    def __str__(self):
        
        return f"numero sala: {self.n}, film: {self.film}, posti: {self.posti_totali}"
    


s: Sala = Sala(1, f, 100)

#s.prenota_posti(1)

#print(s)


class Cinema:

    def __init__(self):

        self.sale: list[Sala] = []
    
    def aggiungi_sala(self, sala: Sala):

        if self.sale == []:

            self.sale.append(sala)

            print("sala aggiunta con successo")
        
        else:




            for i in self.sale:

                if i.get_n() == sala.get_n():

                    raise Exception("non possono esserci sale con lo stesso numero")
            
                else:

                    self.sale.append(sala)

                    print("sala aggiunta con successo")
        
    def __str__(self):

        return f"elenco sale con i relativi film: {self.sale}"
    
    def prenota_film(self, titolo_film: str, num_posti: int):

        
        for i in self.sale:

            if i.get_film().get_titolo() == titolo_film:

                if num_posti <= i.posti_disponibili():

                    i.prenota_posti(num_posti)

                    




c: Cinema = Cinema()

c.aggiungi_sala(s)

c.prenota_film("il cavaliere oscuro", 5)


    

    
    
    
    
    


    

      
        

        

        
    
    
    
    


            


        
    



        

    
    
    