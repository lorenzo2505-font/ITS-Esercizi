'''16. Filtrare e classificare i numeri

Progettare un algoritmo che consenta all’utente di inserire 10 numeri interi.
L'algoritmo deve:

contare quanti numeri sono positivi e quanti sono negativi,
verificare quanti numeri positivi sono pari e maggiori di 20,
verificare quanti numeri negativi sono dispari o minori di -10.
Mostrare in output i conteggi distinti per ogni categoria.

'''

i=1
positivi_pari_e_maggiori = 0
negativi_dispari_o_minori = 0
while i <= 10:
    n = int(input("inserisci numero: "))
    i+=1
    if (n >= 0) and (n % 2 == 0) and (n  > 20):
        positivi_pari_e_maggiori+=1
    if (n < 0) and (n % 2 != 0) or (n < -10):
        negativi_dispari_o_minori+=1
print(positivi_pari_e_maggiori)
print(negativi_dispari_o_minori)
    