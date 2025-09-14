'''Scrivi una funzione extract_emails(text) che prende un testo e restituisce tutte le email trovate.'''

import re

def extract_emails(text: str) -> list[str]:

    email_occ: list[str] = re.findall(r"[A-Za-z0-9]+@[A-Za-z0-9]+.[A-Za-z0-9]+", text)

    return email_occ


print(extract_emails("Contattaci a info@azienda.com oppure support@help.org"))
