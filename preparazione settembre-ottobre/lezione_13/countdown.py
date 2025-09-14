def countdown(n:int) -> None:

    # n is negative
    if n < 0 :
        print("Error! Inserted number is negative!")

    # other cases
    else:
        print(n)
        countdown(n-1)
        
countdown(5)
