import re

text:str = "Il codice è: 123-ABC"
match = re.search(r"(\d+)-([A-Z]+)", text)

if match:
    print("Intera corrispondenza:", match.group(0)) # Output: "123-ABC"
    print("Gruppo 1 (numeri):", match.group(1)) # Output: "123"
    print("Gruppo 2 (lettere):", match.group(2)) # Output: "ABC"

 