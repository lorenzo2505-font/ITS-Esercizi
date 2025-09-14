

'''1. Sistema di valutazione scolastica:

Crea una funzione che accetti come input il nome di uno studente e i suoi punteggi nelle diverse materie.
La funzione calcola il punteggio medio e visualizza il nome dello studente, la media e un messaggio che 
indica se lo studente ha superato l'esame (media >= 60) o meno.
Crea un ciclo for per iterare su un elenco di studenti e punteggi, chiamando la funzione per ogni studente.'''


def valutazioneScolastica(nome: str, voti: list[float]):
    media = sum(voti) / len(voti)

    print(f"nome studente: {nome}")
    print(f"media: {media.__round__()}")

    if media >= 60:

        print("lo studente ha superato l'esame")
    
    else:

        print("lo studente NON ha superato l'esame")



studenti_e_punteggi: dict[str, list[float]] = {"lorenzo rossi": [70.0, 80.0, 90.0], "alessandro popa": [60.0, 80.0, 90.0], "roberto delisio": [100.0, 100.0, 100.0]}

for key, value in studenti_e_punteggi.items():
    
    valutazioneScolastica(key, value)



    


