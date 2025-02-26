'''5-1. Test condizionali: scrivere una serie di test condizionali. Stampa una dichiarazione
descrivendo ciascun test e la tua previsione per i risultati di ciascun test. Il tuo codice
dovrebbe assomigliare a questo:
macchina = 'subaru'
print("L'auto è == 'subaru'? Prevedo Vero.")
print(macchina == 'subaru')
print("\nL'auto == 'audi'? Prevedo Falso.")
print(macchina == 'audi')
• Osserva attentamente i risultati e assicurati di comprendere il motivo di ogni riga
restituisce Vero o Falso.
• Creare almeno 10 test. Avere almeno 5 test che valutano Vero e un altro
5 test valutano Falso.'''

macchina = str(input("inserisci macchina: "))
predict: bool

if macchina == "Yaris":
    predict = True
    print(f"{macchina}, {predict}")
elif macchina == "Audi":
    predict = True
    print(f"{macchina}, {predict}")
elif macchina == "Smart":
    predict = True
    print(f"{macchina}, {predict}")
elif macchina == "Fiat":
    predict = True
    print(f"{macchina}, {predict}")
elif macchina == "Volkswagen":
    predict = True
    print(f"{macchina}, {predict}")
elif macchina == "Lancia":
    predict = False
    print(f"{macchina}, {predict}")
elif macchina == "BMW":
    predict = False
    print(f"{macchina}, {predict}")
elif macchina == "Mercedes":
    predict = False 
    print(f"{macchina}, {predict}")
elif macchina == "Porsche":
    predict = False
    print(f"{macchina}, {predict}")
elif macchina == "Ferrari":
    predict = False
    print(f"{macchina}, {predict}")
else:
    print("La macchina che hai inserito non rientra nei predicts")
    