i=1
massimo_vendite = 0
minimo_vendite=10000000000
massimo_nome: str
minimo_nome: str
while i <= 5:
    nome_venditore = str(input("inserisci il nome del venditore: "))
    totale_vendite = int(input("inserisci il totale delle vendite: "))
    i+=1
    if totale_vendite > massimo_vendite:
        massimo_vendite = totale_vendite
        massimo_nome = nome_venditore
    if totale_vendite <= minimo_vendite:
        minimo_vendite = totale_vendite
        minimo_nome = nome_venditore
        
print(f"il valore più alto di vendite è {massimo_vendite} e il nome associato è: {massimo_nome}")
print(f"il valore più basso di vendite è {minimo_vendite} e il nome associato è: {minimo_nome} ")






    