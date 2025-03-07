#esercizio migliorato 
alphabet=["A","B","C","D","E"]
first_letter= "A"
last_letter= "E"
first_three=(alphabet[0:3])
last_three=(alphabet[2:5])
print(first_three)
print(last_three)
alphabet.extend(["F", "G", "H"])
last_three=(alphabet[5:8])
print(last_three)
alphabet.remove("H")
last_three.remove("H")
print(last_three)




