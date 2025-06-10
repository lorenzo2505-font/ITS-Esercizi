'''Scrivi una funzione extract_emails(text) che prende un testo e restituisce tutte le email trovate.

Esempio:

text = "Contattaci a info@azienda.com oppure support@help.org"
extract_emails(text)  # ['info@azienda.com', 'support@help.org']'''

import re



def extract_emails(text: str):


    emails = re.findall(r"[A-Za-z0-9]+@[A-Za-z0-9]+.[A-Za-z0-9]{2,}", text)

    return emails


test = extract_emails("Contattaci a info@azienda.com oppure support@help.org")

print(test)
 









