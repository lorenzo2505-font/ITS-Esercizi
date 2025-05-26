'''Conversione in numeri romani:

Crea una funzione che converta un dato numero intero nella sua rappresentazione in numeri romani.

Gestisci numeri da 1 a 3999.

Utilizza una combinazione di manipolazione di stringhe e istruzioni condizionali per costruire il numero romano.'''

#fallito
def roman(n: int) -> str:

    

    numero_romano: str = ""



    if n < 1 or n > 3999:

        return f"il numero non rientra nell'intervallo"
    
    else:

        n_string = str(n)

        for i in range(len(n_string)):

            if int(n_string[i]) in range (1, 4 + 1):

                numero_romano += "I" * int(n_string[i])
            
            if int(n_string) == 5:

                pass



#versione prof


# Function to convert an integer to a Roman numeral
def int_to_roman(num: int) -> str:
    # List of Roman numeral values in descending order
    val: list[int] = [
        1000, 900, 500, 400,
        100, 90,  50,  40,
        10, 9,    5,   4, 1
    ]
    
    # Corresponding Roman numeral symbols for the values
    syms: list[str] = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]
    
    # Resulting Roman numeral string to be built
    roman: str = ""

    # Iterate through the values and symbols
    for i in range(len(val)):
        # While the current value can be subtracted from num
        while num >= val[i]:
            roman += syms[i]     # Append the corresponding symbol
            num -= val[i]        # Subtract the value from num

    # Return the constructed Roman numeral
    return roman

# Example usage of the function
print(int_to_roman(1994))  # Output: MCMXCIV


        

        

            
            
        

