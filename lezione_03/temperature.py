'''Sviluppare un algoritmo che chieda all’utente di inserire 7 temperature
 (una per ogni giorno della settimana). L'algoritmo deve:

calcolare la temperatura media,
controllare se tutte le temperature sono comprese tra 10 e 30:
Se sì, mostrare “Temperatura nella norma”.
verificare se almeno una temperatura è maggiore di 35 o minore di 5:
Se sì, mostrare “Allerta temperatura”.
Mostrare in output la media, il giorno della temperatura più alta 
e il giorno della temperatura più bassa espresso numericamente (es. 1 per lunedì, 2 per martedì, ecc.).'''

i = 1
norma = 0
somma = 0
temp_max = 0
temp_min = 10000000000000000000000
giorno_max: str
giorno_min: str
while i <= 7:
    giorno = str(input("inserisci giorno: "))
    temp = int(input("inserisci temperatura: "))
    i+=1
    if (temp >= 10) and  (temp <= 30):
        norma+=1
    if (temp > 35) or (temp < 5):
        print("allerta temperatura")
    somma = somma + temp
    media = somma / i
    if temp > temp_max:
        temp_max = temp
        giorno_max = giorno
    if temp  < temp_min:
        temp_min = temp
        giorno_min = giorno




if norma == 7:
    print("temperature nella norma")

print(media)

print(f"il giorno con la temperatura più alta è stato {giorno_max}, {temp_max} gradi celsius")
print(f"il giorno con la temperatura più bassa è stato {giorno_min}, {temp_min} gradi celsius")



