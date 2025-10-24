def calculate_std_dev(nums: list[float]) -> float:
    
    if not(nums):
        raise ValueError("la lista è vuota")
    
    somma = 0
    l = 0

    for i in nums:
        somma += i
        l += 1
    
    media = somma / l
    new_sum = 0

    for el in nums:
        new_sum += (el - media)**2
    
    varianza = new_sum / l
    dev_std = varianza ** 1/2

    return dev_std

    

if __name__ == '__main__':
    
    print(calculate_std_dev([1.0, 2.0, 3.0, 4.0, 5.0]))
