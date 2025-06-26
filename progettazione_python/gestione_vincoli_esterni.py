class Persona:

    def __init__(self, *, nome: str,
                  is_studente: bool = False,
                    matricola: int|None = None, 
                    corso_iscritto: str|None = None):
        
        if ((is_studente != matricola is not None) or (is_studente != corso_iscritto is not None)):

            raise ValueError("") 