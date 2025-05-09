
import re
text:str = "My email is marco@gmail.com"
result:list[str] = re.findall(r'\S+@\S+', text)
print(result) # Output ['marco@gmail.com']

 