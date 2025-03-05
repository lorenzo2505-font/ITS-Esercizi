'''Progettare un algoritmo che simuli il comportamento di un semaforo intelligente.
 Questo sistema deve adattare i tempi di durata (espressi in percentuale)
   del verde in base al numero di veicoli presenti sulle principali direzioni di traffico: 
   Nord-Sud ed Est-Ovest. Ogni direzione può ricevere una priorità se il numero di veicoli 
   supera una soglia predefinita.

Requisiti:

Se il numero di veicoli in una sola direzione supera la soglia (es. 70 veicoli),
 quella direzione riceve un tempo minimo garantito per il verde (es. 60%) e il restante tempo è assegnato
   all'altra direzione.
Se entrambe le direzioni superano la soglia, il tempo è equamente suddiviso 
(50% per ciascuna direzione).
Se nessuna direzione supera la soglia, il tempo è calcolato proporzionalmente 
al numero totale di veicoli nelle due direzioni.'''

soglia = int(input("inserisci la soglia: ")) 
Veicoli_Nord_Sud = int(input("quanti veicoli ci stanno nella direzione Nord-Sud ? : "))
Veicoli_Est_Ovest = int(input("quanti veicoli ci stanno nella direzione Est-Ovest ? : "))
Tempo_Nord_Sud: int = None
Tempo_Est_Ovest: int = None
if Veicoli_Nord_Sud  > soglia:
    Tempo_Nord_Sud = 60
    Tempo_Est_Ovest = 40
if Veicoli_Est_Ovest  > soglia:
    Tempo_Est_Ovest  = 60
    Tempo_Nord_Sud = 40
if (Veicoli_Nord_Sud  > soglia) and (Veicoli_Est_Ovest > soglia):
    Tempo_Nord_Sud = 50
    Tempo_Est_Ovest = 50
if (Veicoli_Nord_Sud < soglia) and  (Veicoli_Est_Ovest < soglia):
    Tempo_Nord_Sud = (Veicoli_Nord_Sud) / (Veicoli_Nord_Sud + Veicoli_Est_Ovest) * (100)
    Tempo_Est_Ovest = (Veicoli_Est_Ovest) / (Veicoli_Nord_Sud + Veicoli_Est_Ovest) * (100)
print(Tempo_Nord_Sud)
print(Tempo_Est_Ovest)

