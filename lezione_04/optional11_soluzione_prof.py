
'''def eratostene (n: int):

    if n <=2:

        raise ValueError(f"{n} deve essere maggiore di 2")
    
    setaccio = [i for i in range(2, n)]'''



def fun2 (limit: int):

    is_prime: list[bool] = [True] * (limit + 1)

    is_prime[0:2] = [False, False]

    for i in range(2, int(limit ** 0.5) + 1):

        for j in range(i * i, limit + 1, i):

            is_prime[j] = False
    
    primes: list[int] = [i for i, prime in enumerate(is_prime) if prime]

    return primes


print(fun2(30))



