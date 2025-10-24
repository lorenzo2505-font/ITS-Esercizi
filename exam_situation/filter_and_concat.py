def filter_and_concat(nums: list[int], min_val: int) -> str:
    s = ""

    for el in nums:
        
        if el > min_val:
            s += f"{el},"
    
    return s[0:-1]


if __name__ == '__main__':

    print(filter_and_concat([1, 2, 3, 4, 5], 2))