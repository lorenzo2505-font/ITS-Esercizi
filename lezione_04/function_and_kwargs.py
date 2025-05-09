#il comando **kwargs permette di passare un numero illimitato di argomenti, come un dizionario

#esempio

def total_price (**kwargs):
    total: float = 0
    for product, price in kwargs.items():
        print(f"{product}: {price}")
        total = total + price 
    return round(total, 2)
print(total_price(cofee = 1.5, juice = 1.5))
