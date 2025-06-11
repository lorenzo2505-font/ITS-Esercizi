'''Scrivi una funzione find_fc(text) che trova tutti i codici fiscali all'interno di un testo.

Esempio:

testo = "Mario Rossi CF: RSSMRA85M01H501Z, mentre Maria Bianchi ha il CF BNCMRA85T41H501Y."
codici = find_fc(testo) # ['RSSMRA85M01H501Z', 'BNCMRA85T41H501Y']'''


import re



def find_fc(text: str) -> list:


    fcs = re.findall(r"[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}", text)

    return fcs



test = find_fc("Mario Rossi CF: RSSMRA85M01H501Z, mentre Maria Bianchi ha il CF BNCMRA85T41H501Y.")


print(test)