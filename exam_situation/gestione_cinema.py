class Ticket:
    
    def __init__(self, ticket_id: str, movie: str, seat: str):
        self.ticked_id = ticket_id
        self.movie = movie 
        self.seat = seat
        self.is_booked: bool = False
    
    def book(self) -> None:

        if not(self.is_booked):
            self.is_booked = True
        
        else:
            print(f"Il biglietto per '{self.movie}' posto '{self.seat}' è già prenotato.")
    
    def cancel(self) -> None:

        if self.is_booked:
            self.is_booked = False
        
        else:
            print(f"Il biglietto per '{self.movie}' posto '{self.seat}")
    

class Viewer:

    def __init__(self, viewer_id: str, name: str):
        self.viewer_id = viewer_id
        self.name = name 
        self.booked_tickets: list[Ticket] = []
    
    def book_ticket(self, ticket: Ticket) -> None:
        
        if not(ticket.is_booked):
            self.booked_tickets.append(ticket)
            ticket.book()
        
        else:
            print(f"Il biglietto per '{ticket.movie}' non è disponibile.")
    
    def cancel_ticket(self, ticket: Ticket) -> None:

        if ticket in self.booked_tickets:
            self.booked_tickets.remove(ticket)
            ticket.cancel()
        
        else:
            print(f"Il biglietto per '{ticket.movie}' non è stato prenotato da questo spettatore.")


class Cinema:

    def __init__(self):
        self.tickets: dict[str, Ticket] = {}
        self.viewers: dict[str, Viewer] = {}
    
    def  add_ticket(self, ticket_id: str, movie: str, seat: str) -> None:
        
        if ticket_id in self.tickets:
            print(f"Il biglietto con ID '{ticket_id}' esiste già.")
        
        else:
            self.tickets[ticket_id] = Ticket(ticket_id, movie, seat)
    
    def register_viewer(self, viewer_id: str, name: str) -> None:

        if viewer_id in self.viewers:
            print(f"Lo spettatore con ID '{viewer_id}' è già registrato.")
        
        else:
            self.viewers[viewer_id] = Viewer(viewer_id, name)
    
    def book_ticket(self, viewer_id: str, ticket_id: str) -> None:

        if viewer_id in self.viewers and ticket_id in self.tickets:
            self.viewers[viewer_id].book_ticket(self.tickets[ticket_id])
        
        else:
            print("Spettatore o biglietto non trovato.")
    
    def cancel_ticket(self, viewer_id: str, ticket_id: str) -> None:

        if viewer_id in self.viewers and ticket_id in self.tickets:
            self.viewers[viewer_id].cancel_ticket(self.tickets[ticket_id])
        
        else:
            print("Spettatore o biglietto non trovato.")
    
    def list_available_tickets(self) -> list[str]:
        available_tickets: list[str] = []
        
        for i in self.tickets:

            if not(self.tickets[i].is_booked):
                available_tickets.append(i)
        
        return available_tickets
    
    def list_viewer_bookings(self, viewer_id: str) -> list[str] | str:
        viewer_bookings: list[str] = []

        if viewer_id in self.viewers:
            
            for i in self.viewers[viewer_id].booked_tickets:
                viewer_bookings.append(i.ticked_id)

            return viewer_bookings
        
        else:
            return "Errore: spettatore non trovato."

        


        

    

        

        


        

        
 




        
    



if __name__ == '__main__':
    
    t: Ticket = Ticket('1', 'il cavaliere oscuro', '2')
    t.book()
    t.cancel()

    v: Viewer = Viewer('3', 'lorenzo')
    v.book_ticket(t)
    v.cancel_ticket(t)

    c: Cinema = Cinema()
    c.add_ticket(t.ticked_id, t.movie, t.seat)
    c.register_viewer(v.viewer_id, v.name)
    c.book_ticket('3', '1')
    c.cancel_ticket('3', '1')





        
    

    
