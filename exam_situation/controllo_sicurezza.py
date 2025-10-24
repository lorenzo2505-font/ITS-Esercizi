def check_security_alarm(s1: bool, s2: bool, s3: bool) -> str:
    
    if s1 and (s2 or s3):
        return "Allarme Attivato"
    
    return "Nessun Allarme"


if __name__ == '__main__':

    print(check_security_alarm(False, False, True))
