import re

'''re.match()'''



print(re.match(r"\d+", "123abc")) #controlla un match solo all'inizio di una stringa  
#matches 123


'''re.search()'''

print(re.search(r"\d+", "abc123")) #scansiona la stringa del primo match da qualsiasi parte
# Matches: 123

'''re.fullmatch()'''

print(re.fullmatch(r"\d+", "123")) #controlla se l'intera stringa combacia con il modello RegEx 
# Matches: 123

'''re.findall()'''

print(re.findall(r"\d\d", "12345")) #restituisce una lista di tutti i match non sovrapposti
# Output: ['12', '34']

'''re.finditer()'''

for m in re.finditer(r"\d+", "a1b2"): #restituisce un iteratore di oggetti corrispondenti per tutti i match
    print(m.group())
# Matches: 1 (first iter)
# Matches: 2 (second iter)


'''re.sub()'''

print(re.sub(r"\d", "#", "a1b2")) #restituisce i match con un altra stringa
# Output: 'a#b#'


'''re.split()'''

print(re.split(r"\d+", "a1b2c3")) #splitta una stringa per ogni match
# Output: ['a', 'b', 'c', '']

'''re.compile()'''

pattern = re.compile(r"\d+")
print(pattern.findall("a1b2")) #compila una regex in un regex object per il riutilizzo
# Matches: ['1', '2'] 

 