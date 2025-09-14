'''Dato un array binario nums, dovresti eliminarne un elemento.

Restituisce la dimensione del sottoarray non vuoto più lungo contenente solo 1 nell'array risultante.
Restituisce 0 se non esiste alcun sottoarray di questo tipo.'''

def binary_array(nums: list[int], index: int):
    
    max = False

    for n in nums:

        if n != 0 and n != 1:

            raise ValueError("this array contains only binary numbers, so only 0 or 1")
    
    if index > len(nums) - 1:

        raise IndexError(f"index: {index} out of range")
    
    nums.pop(index)

    binary_string: str = ""

    for i in nums:
        binary_string += str(i)
    
    newlist: list = binary_string.split("0")
    
    for i in range(len(newlist)):

        if len(newlist[i]) > max or max is False:
            max = len(newlist[i])
    
    return max


if __name__ == "__main__":

    print(binary_array( [1, 1, 1], 2))

    
    

        
    

            
    


            
            
            

    
    

        
    
        