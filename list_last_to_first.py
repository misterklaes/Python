lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if len(lst) > 1 and bool(lst) == True:
    lst.insert(0, lst.pop())
    print(lst)  # [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]
else:
    print("Список пустий або надто малий для переміщення елементів.")
    print(lst)  # [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]