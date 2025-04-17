import re

text:str = "123-ABC"

new_text:str = re.sub(r"(\d+)-([A-Z]+)", r"\2-\1", text)

print(new_text) # Output: "ABC-123"


 
