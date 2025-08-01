lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#lst = []
if len(lst) == 0:
    result = [[],[]]
    print("Список списків", result)
else:
    lst_divided_num = len(lst) // 2
    if len(lst) % 2 == 0:
        first_sub_list = lst[:lst_divided_num]
        second_sub_list = lst[lst_divided_num:]
    else:
        first_sub_list = lst[:lst_divided_num + 1]
        second_sub_list = lst[lst_divided_num + 1:]
    result = [first_sub_list, second_sub_list]
    print("Список у якому елементи теж списки:", result)