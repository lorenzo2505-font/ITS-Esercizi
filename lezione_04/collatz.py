import matplotlib as plt 

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





def collatz (num: float):

    mylist: list = [num]

    while num != 1:

        if num % 2 == 0:

            num = num / 2

        else:

            num = (3 * num) + 1

        mylist.append(num)

    return mylist


mylist2: list [float] = collatz(8.0)

plt.plot(mylist2)

plt.show ()


