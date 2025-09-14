# - file handling
    # r - Read: apre file, errore se non esiste
    # a - Append: apre per appendere, crea se non esiste
    # w - Write: apre per scrivere, crea se non esiste
    # x - Create: crea il file, errore se non esiste

# - aprire un file
# - leggere un file
# - scrivere in un file
# - creare un file
# - eliminare file (check) e eliminare cartella


def aprire_file():

    f = open("lezione_15/numb.txt", "r")
    #print(f.read())
    print(f.readline())
    print(f.readline())


#aprire_file()



def più_righe():

    f = open("lezione_15/numb.txt", "r")

    for riga in f:
        print(riga)
    
    f.close() # chiudere il file

#più_righe()


def aggiungere():

    f = open("lezione_15/testo.txt", "a")
    f.write("scrivo ciò che voglio")
    f.close()

    f = open("lezione_15/testo.txt", "r")
    print(f.read())


#aggiungere()


def creare_file():

    f = open("lezione_15/crearefile.txt", "x")











