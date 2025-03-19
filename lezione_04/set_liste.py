def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    second_set = set()
    for i in elements_to_remove:
        second_set.add(elements_to_remove[i])
    original_set.update(second_set)

    return original_set

print(remove_elements({5, 6, 7}, [7, 8, 9]))