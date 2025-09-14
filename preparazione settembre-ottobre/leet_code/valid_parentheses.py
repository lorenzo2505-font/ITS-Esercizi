'''Data una stringa s contenente solo i caratteri '(', ')', '{', '}', '[' e ']', determinare se la stringa di input è valida.

Una stringa di input è valida se:

Le parentesi aperte devono essere chiuse con parentesi dello stesso tipo.
Le parentesi aperte devono essere chiuse nell'ordine corretto.
Ogni parentesi chiusa ha una parentesi aperta corrispondente dello stesso tipo.'''


def valid_parentheses(s: str):

    parentheses: list[str] = ["(",  "[",  "{", ")", "]", "}"]
    
    for i in range(len(s)):
        
        if s[i] == "(":

            if ")" in s[i:] and s[i + 1] != "]" and s[i + 1] != "}":
                continue

            return False

        elif s[i] == "[":
            
            if "]" in s[i: ] and s[i + 1] != ")" and s[i + 1] != "}":
                continue

            return False
            

        elif s[i] == "{":
            
            if "}" in s[i: ] and s[i + 1] != ")" and s[i + 1] != "]":
                continue

            return False

        else:
            
            if (s[i] not in parentheses) or (s[i] not in parentheses):

                return False
    
    return True

print(valid_parentheses("()"))
print(valid_parentheses("()[]{}"))
print(valid_parentheses("(]"))
print(valid_parentheses("([])"))
print(valid_parentheses("([)]"))


    
    