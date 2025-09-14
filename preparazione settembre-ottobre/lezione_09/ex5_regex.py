'''Scrivi una funzione find_dates(text) che trova tutte le date in formato italiano (dd/mm/yyyy) in un testo.'''
import re

def find_dates(text: str):

    occ_date: list = re.findall(r"[0-9]{2}/[0-9]{2}/[0-9]{4}", text)

    return occ_date

print(find_dates("Le date importanti sono 09/04/2025 e 15/08/2023."))
