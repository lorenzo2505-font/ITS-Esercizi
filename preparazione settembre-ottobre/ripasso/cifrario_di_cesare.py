from string import ascii_lowercase
from string import ascii_uppercase

def caesar_cypher_encrypt(s: str, key: int):
    l = ascii_lowercase
    u = ascii_uppercase
    parola_encriptata: str = ""

    while key > 26:
        key -= 26
    
    for i in range(len(s)):
        
        if s[i] in l:

            for j in range(len(l)):

                if l[j] == s[i]:
                    

                    parola_encriptata += l[(j + key) % len(l)] # l'operatore modulo da il resto della divisione evitando l'index error
                    
        elif s[i] in u:

            for j in range(len(u)):

                if u[j] == s[i]:
                    parola_encriptata += u[(j + key) % len(u)] # l'operatore modulo da il resto della divisione evitando l'index error
        
        else:
            parola_encriptata += s[i]
    
    return parola_encriptata



t = caesar_cypher_encrypt("simone zazza", 3)
print(t)

def caesar_cypher_decrypt(s: str, key: int):
    
    l = ascii_lowercase
    u = ascii_uppercase
    parola_decriptata: str = ""

    while key > 26:
        key -= 26
    
    for i in range(len(s)):

        if s[i] in l:

            for j in range(len(l)):

                if l[j] == s[i]:
                    parola_decriptata += l[(j - key) % len(l)]
        
        elif s[i] in u:

            for j in range(len(u)):

                if u[j] == s[i]:
                    parola_decriptata += u[(j - key) % len(u)]
        
        else:
            parola_decriptata += s[i]
    
    return parola_decriptata

print(caesar_cypher_decrypt(t, 3))





    
