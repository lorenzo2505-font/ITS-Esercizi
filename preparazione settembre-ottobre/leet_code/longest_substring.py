'''Data una stringa s, trova la lunghezza della sottostringa più lunga senza caratteri duplicati.'''

def longest_substring(s: str) -> int:

    lista: list = []
    len_list: list = []

    for i in range(len(s)):
        
        if s[i] not in lista:
            lista.append(s[i])
        
        else:
            len_list.append(len(lista))
            lista.clear()
            lista.append(s[i])
    
    return max(len_list)

print(longest_substring("abcabcbb"))
print(longest_substring("bbbbb"))
print(longest_substring("pwwkew"))

        
        

