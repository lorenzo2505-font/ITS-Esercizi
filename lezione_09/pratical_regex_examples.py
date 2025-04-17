
#1. Starts with capital?
import re
text:str = "Rome Paris"
result = re.match(r'[A-Z][a-z]+', text)
print(result.group()) # Output "Rome"


#2. Find numbers:
import re
text:str = "I have 20 cats and 3 dogs"
numbers:list[str] = re.findall(r'\d+', text)

print(numbers) # Output ['20', '3']



 