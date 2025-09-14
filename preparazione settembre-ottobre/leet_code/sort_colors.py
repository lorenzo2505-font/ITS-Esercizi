
def sort_colors(nums: list[int]) -> list[int]:
    
    colors: list[str] = []
    newlist: list[int] = []

    for i in nums:

        if i not in range(0, 2 + 1):

            raise ValueError(f"{i} non è un numero compreso tra 0 e 2")
        
        if i == 0:
            colors.append("red")
        
        if i == 1:
            colors.append("white")
        
        if i == 2:
            colors.append("blue")
    
    for color in colors:

        if color == "red":
            newlist.insert(0, 0)
        
        if color == "white":
            newlist.insert(1, 1)
        
        if color == "blue":
            newlist.insert(2, 2)
    
    return newlist

print(sort_colors([2,0,2,1,1,0]))
print(sort_colors([2,0,1]))