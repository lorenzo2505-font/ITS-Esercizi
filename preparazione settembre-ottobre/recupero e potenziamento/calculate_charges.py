
def calculate_charges(hours: int) -> float:

    if hours > 24:
        
        raise ValueError("nessuna macchina può essere parcheggiata per più di 24 ore")
    
    m = hours % 1

    if m > 0:
        hours += 1 - m

    
    if hours <= 3:
        prezzo = 2.0
    
    elif hours == 24:
        prezzo = 10
    
    else:
        prezzo = 2.0 + (0.5 * (hours - 3))
        
        if hours % 1 != 0:
            prezzo += 0.5
    
    return prezzo


def main():

    print(calculate_charges(1.5))
    print(calculate_charges(4))
    print(calculate_charges(5.5))
    print(calculate_charges(24))




main()