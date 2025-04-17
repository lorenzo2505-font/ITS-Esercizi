import re

text:str = "abcabcabc"

print("Cattura:", re.findall(r"(abc)+", text)) # Output ['abc']
print("Non cattura:", re.findall(r"(?:abc)+", text)) # Output ['abcabcabc’]

'''Suggerimenti per gli studenti
• Utilizzare gruppi di cattura solo quando è necessario estrarre parti della corrispondenza.
• Utilizzare gruppi non di cattura quando è necessario raggruppare solo per ripetizione o logica, non per restituire dati.'''


#r "(abc)+" Capturing Group

#r "(?:abc)+" None Capturing Group



