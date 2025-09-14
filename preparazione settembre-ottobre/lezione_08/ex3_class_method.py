from __future__ import annotations

class Libro:

    def __init__(self, titolo: str, autore: str, isbn: str):
        
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
        
    
    def __str__(self):
        
        return f"titolo: {self.titolo}, autore: {self.autore}, codice isbn: {self.isbn}"
    
    @classmethod

    def from_string(cls, mystr: str):
        
        string_list = mystr.split(", ")

        cls.libro = Libro(titolo = string_list[0], autore = string_list[1], isbn = string_list[2])
        
        return cls.libro






class Membro:
    
    def __init__(self, nome: str, member_id: str):
        
        self.nome = nome
        self.member_id = member_id
        self.borrowed_books: list[Libro] = []
    
    def borrow_book(self, libro: Libro):

        if libro in self.borrowed_books:

            raise ValueError("il libro è già stato noleggiaato")
        
        self.borrowed_books.append(libro)

    def return_book(self, libro: Libro):

        if libro not in self.borrowed_books:

            raise ValueError("il libro non è mai stato noleggiato")
        
        self.borrowed_books.remove(libro)
    
    def __str__(self):
        
        return f"nome membro: {self.nome}, id membro: {self.member_id}, libri noleggiati: {self.borrowed_books}"
    
    @classmethod
    
    def from_string(cls, mystr: str):

        string_list = mystr.split(", ")
        
        cls.membro = Membro(nome = string_list[0], member_id = string_list[1])

        return cls.membro


class Biblioteca:

    total_books = 0

    def __init__(self):
        
        self.libri: list[Libro] = []
        self.membri: list[Membro] = []
    
    def add_book(self, libro: Libro):
        
        if libro in self.libri:

            raise ValueError("il libro è già presente nell'elenco")
        
        self.libri.append(libro)
        Biblioteca.total_books += 1
    
    def remove_book(self, libro: Libro):

        if libro not in self.libri:
            
            raise ValueError("il libro non è presente nell'elenco")
        
        self.libri.remove(libro)
        Biblioteca.total_books -= 1
    
    def register_member(self, membro: Membro):

        if membro in self.membri:
            
            raise ValueError("il membro è già registrato")
        
        self.membri.append(membro)
    
    def lend_book(self, libro: Libro, membro: Membro):

        if libro not in self.libri:
            
            raise ValueError("il libro non è presente nell'elenco")
        
        if membro not in self.membri:

            raise ValueError("l'utente non è registrato")
        
        membro.borrow_book(libro)
        self.remove_book(libro)
    
    def __str__(self):
        
        return f"libri: {self.libri}, membri: {self.membri}"
    
    @classmethod

    def library_statistics(cls):

        print(f"totale libri: {cls.total_books}")



def main():

    string_book1: str = "il visconte dimezzato, italo calvino, 1"
    il_visconte_dimezzato: Libro = Libro.from_string(string_book1)

    string_book2: str = "se questo è un uomo, primo levi, 2"
    se_questo_è_un_uomo: Libro = Libro.from_string(string_book2)

    string_book3: str = "bro code, barney stinson, 3"
    bro_code: Libro = Libro.from_string(string_book3)

    string_member1: str = "alessandro popa, torvaianica"
    popa: Membro = Membro.from_string(string_member1)

    string_member2: str = "marco pierlions, termini"
    pierlions: Membro = Membro.from_string(string_member2)

    string_member3: str = "lorenzo rossi, aranova"
    rossi: Membro = Membro.from_string(string_member3)

    biblioteca_its: Biblioteca = Biblioteca()

    biblioteca_its.register_member(popa)
    biblioteca_its.register_member(pierlions)
    biblioteca_its.register_member(rossi)

    biblioteca_its.add_book(il_visconte_dimezzato)
    biblioteca_its.add_book(se_questo_è_un_uomo)
    biblioteca_its.add_book(bro_code)

    biblioteca_its.lend_book(il_visconte_dimezzato, popa)
    print(biblioteca_its)

    biblioteca_its.lend_book(se_questo_è_un_uomo, pierlions)
    print(biblioteca_its)

    biblioteca_its.lend_book(bro_code, rossi)
    print(biblioteca_its)


main()









    

    



    
        