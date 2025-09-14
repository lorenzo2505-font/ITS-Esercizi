#REGEX




# Concetti chiave

# - sono stringhe

# - possonono contenere qualsiasi carattere

# (- metacaratteri: . ^ $ * + ? {} [] () \ |)

#versione lunga
import re

pattern = re.compile(r"l+") # con re.l considera anche la L maiuscola

lista = pattern.findall("elliot alderson")

print(lista)


#versione abbreviata

mylist = re.findall(r"l+", "elliot alderson")

print(mylist)

'''

metodi di ricerca:

- findall ()

- search () # ritorna la prima occorrenza di un pattern in un testo

- match () # verifica se il pattern esiste all'inizio del testo'''






match_obj = re.search(r"l+", "elliot alderson")

print(match_obj)


'''


Metodi dei match objects:

- group () # ritrona il pattern 

- start () # ritorna l'indice dal quale inizia il pattern

- end ()''' # ritorna l'indice dal quale finisce il pattern



mo = re.search(r"sam", "elliot alderson e sam sapiol")

print("{} inizia a {} e finisce a {}".format(mo.group(), mo.start(), mo.end()))



#scrivere la regex


parola = re.findall(r"l[aeiou]+", "elliot alderson") #lettera l seguita da una consonante

print(parola)


parola2 = re.findall(r"[a-d]+", "elliot alderson") #tutte le parole comprese tra acd

print(parola2)


parola3 = re.findall(r"[0-9]", "elliot alderson 9")

print(parola3)


parola4 = re.findall(r"[^0-9]", "elliot alderson") # quel ^ indica l'opposto di ciò che è stato indicato

print(parola4)


parola5 = re.findall(r"b[aeiou]ll", "bill gates drinks red bull") # altro esempio

print(parola5)


# sequenze speciali

'''
\d -> numero

\D -> non numero [^0-9]

\s -> spazio bianco

\S -> non spazio bianco

\w -> carattere alfanumerico [A-Za-z0-9]

\W -> non carattere alfanumerico [^A-Za-z0-9]

\/ -> forward slash (barra in avanti)

\\ -> backslash (barra indietro)

\" -> double quote

\ ' -> single quote

\n -> newline

^ -> inizio di una stringa

$ -> fine di una stringa

. -> qualsiasi carattere


(whiterose|price|ray) # per usare gli or

operatori di ripetizione:

* -> zero o più volte

+ -> una o più volte

? -> zero o una volta

{p, q} -> almeno p e al massimo q volte

{p,} -> almeno p volte

{p} -> esattamente p volte

'''

