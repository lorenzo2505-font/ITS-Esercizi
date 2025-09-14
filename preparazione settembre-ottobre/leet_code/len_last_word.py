'''Data una stringa composta da parole e spazi, restituisce la lunghezza dell'ultima parola della stringa.

Una parola è una sottostringa massima composta solo da caratteri diversi dagli spazi.'''

def len_last_word(s: str) -> int:

    s_list = s.split(" ")

    return len(s_list[-1])


print(len_last_word("Hello World"))
print(len_last_word("fly me to the moon"))
print(len_last_word("luffy is still joyboy"))