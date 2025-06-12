'''5-7. Frutto preferito: fai un elenco dei tuoi frutti preferiti,
 e poi scrivi una serie di istruzioni if indipendenti che controllino determinati frutti nella tua lista.
• Crea un elenco dei tuoi tre frutti preferiti e chiamalo favorito_frutti.
• Scrivi cinque istruzioni if. Ognuno dovrebbe verificare se un certo tipo di frutta è presente nella tua lista. 
Se il frutto è nella tua lista, il blocco if dovrebbe stampare un'affermazione, come Ti piacciono davvero le mele!'''

frutti_preferiti: list[str] = ["mela", "pesca", "arancia"]

if "mela" in frutti_preferiti:
    print("vedo che ti piacciono le mele")

if "pesca" in frutti_preferiti:
    print("sono buone sopratutto le percoche")

if "arancia" in frutti_preferiti:
    print("quelle sono buone in inverno")

if "melone" in frutti_preferiti:
    print("quello è buono in estate")
    
if "fragola" in frutti_preferiti:
    print("quella è buona in primavera")