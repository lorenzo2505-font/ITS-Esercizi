
class ContactManager:

    def __init__(self):
        
        self.contacts: dict[str, list[str]] = {}
    
    def create_contact(self, name: str, phone_numbers: list[str]) -> dict:

        if name in self.contacts:
            
            raise ValueError("il contatto esiste già")
        
        self.contacts[name] = phone_numbers

        return {name: phone_numbers}
    
    def add_phone_number(self, contact_name: str, phone_number: str) -> dict:
 
        if contact_name not in self.contacts:

            raise ValueError("il contatto non esiste")
        
        if phone_number in self.contacts[contact_name]:

            raise ValueError("il numero di telefono esiste già")
        
        self.contacts[contact_name].append(phone_number)

        return {contact_name: self.contacts[contact_name]}
    
    def remove_phone_number(self, contact_name: str, phone_number: str) -> str: 

        if contact_name not in self.contacts:
            
            raise ValueError("il contatto non esiste")
        
        if phone_number not in self.contacts[contact_name]:

            raise ValueError("il contatto non esiste")
        
        self.contacts[contact_name].remove(phone_number)

        return {contact_name: self.contacts[contact_name]}
    
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str) -> dict:
        
        if contact_name not in self.contacts:
            
            raise ValueError("il contatto non esiste")
        
        if old_phone_number not in self.contacts[contact_name]:

            raise ValueError("Il numero di telefono non esiste")
        
        if new_phone_number in self.contacts[contact_name]:

            raise ValueError("questo numero di telefono è già presente")
        
        for i in range(len(self.contacts[contact_name])):

            if self.contacts[contact_name][i] == old_phone_number:
                self.contacts[contact_name].pop(i)
                self.contacts[contact_name].insert(i, new_phone_number)
                break

        return {contact_name: self.contacts[contact_name]}
    
    def list_contacts(self) -> list:

        return self.contacts.keys()
    
    def list_phone_numbers(self, contact_name: str) -> list[str]: 

        if contact_name not in self.contacts:
            
            raise ValueError("il contatto non esiste")
        
        return self.contacts[contact_name]
    
    def search_contact_by_phone_number(self, phone_number: str) -> list[str]:

        mylist: list[str] = []

        for i in self.contacts:

            if phone_number in self.contacts[i]:
                mylist.append(i)
        
        if not(mylist):
            
            raise ValueError("nessun contatto trovato con questo numero di telefono")
        
        return mylist



def main():

    popa_contacts: ContactManager = ContactManager()

    print(popa_contacts.create_contact("pusher", ["123"]))
    print(popa_contacts.add_phone_number("pusher", "456"))
    print(popa_contacts.remove_phone_number("pusher", "456"))
    print(popa_contacts.update_phone_number("pusher", "123", "789"))
    print(popa_contacts.list_contacts())
    print(popa_contacts.list_phone_numbers("pusher"))
    print(popa_contacts.search_contact_by_phone_number("789"))
    


main()
        
    
    

    
