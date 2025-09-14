mystr: str = "in the end"

mylist: list[int] = [len(i) for i in mystr.split(" ")]

print(mylist)