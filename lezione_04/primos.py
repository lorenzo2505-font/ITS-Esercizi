
def primi(n: int) -> bool:

    i = 0

    divisori = 0

    if n < 2:

        return False
    
    else:

        while i <= n:

            i += 1

            if n % i == 0:

                divisori += 1
            
        if divisori > 2:

            return False
        
        else:

            return True
        

n = primi(4)

print(n)

                
                

