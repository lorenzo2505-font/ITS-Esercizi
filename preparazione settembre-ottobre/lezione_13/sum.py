def recursiveSum(n:int) -> int:

    # n is negative
    if n < 0:
        print("Error! Inserted number is negative!")
        return None
    
    # if n = 0 recursive process must be stopped
    elif n == 0:

        return 0
    # if n is positive, compute recursive sum
    else:

        return int(n + recursiveSum(n-1))

print(recursiveSum(3))