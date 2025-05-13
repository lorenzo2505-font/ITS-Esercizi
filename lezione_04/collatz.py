def fun1 (n1: int):

    if n1 % 2 == 0:
        n1 = n1 / 2

        return n1
    else:

        n1 = (3 * n1) + 1

        return n1
    

def fun2(n2: int):

    r = fun1(n2)

    while True:

        if r == 1:
            break

        r = fun1(r)

    return r 

       

print(fun2(5))
