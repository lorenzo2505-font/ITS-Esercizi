'''4-2. Animali: pensa ad almeno tre animali diversi che hanno una caratteristica comune. Memorizza i nomi di questi animali in un elenco,
 quindi utilizza un ciclo for per stampare il nome di ciascun animale.
• Modificare il programma per stampare una dichiarazione su ciascun animale, ad esempio Un cane sarebbe un ottimo animale domestico.
• Aggiungi una riga alla fine del tuo programma, indicando cosa hanno in comune questi animali.
 Potresti stampare una frase, ad esempio Ognuno di questi animali sarebbe un ottimo animale domestico!'''

animali: list[str] = ["Gatto", "Tigre", "Leone"]

for i in animali:
    print(f"adoro questo animale: {i}")
    
    '''if i == "Gatto":
        print(f"il {i} è un ottimo animale domestico")
    if i == "Tigre":
        print(f"la {i} è il felino più grande") 
    if i == "Leone":
        print(f"il {i} è il re")''' #frase diversa per ogni elemento 


print("tutti questi animali sono dei felini")
