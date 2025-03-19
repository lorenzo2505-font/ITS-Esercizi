def check_access(username: str, password: str , is_active: bool) -> str:
    esito: str = None
    if username == "admin" and password == "12345" and is_active == True:
        esito = "Accesso consentito"
        
    else:
        esito = "Accesso negato"
    return esito

print(check_access("admin", "12345", True))

print(check_access("admin", "54321", True))