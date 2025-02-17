'''Ogni funzione: pensa alle cose che potresti memorizzare in un elenco. 
Ad esempio, potresti creare un elenco di montagne, fiumi, paesi, città, lingue o qualsiasi altra cosa desideri. 
Scrivere un programma che crei un elenco contenente questi elementi
 e quindi utilizzi ciascuna funzione introdotta in questo capitolo almeno una volta.'''

lingue: list = ["Italiano", "Inglese", "Spagnolo", "Tedesco", "Francese", "Olandese", "Portoghese", "Giapponese"]

print(lingue)

print(len(lingue))

print(lingue[0])

print(lingue[-1])

lingue.append("Turco")

print(lingue)

lingue.insert(1, "Arabo")

print(lingue)

lingue.pop(5)

print(lingue)

lingue.remove("Arabo")

print(lingue)

lingue.extend(["Egiziano", "Filippino"])

print(lingue)

#del lingue

print(lingue[0:2])

print(lingue[1:])

print(lingue[:1])

print(lingue[:])

lingue=sorted(lingue)
lingue.reverse()
print(lingue)

del lingue



