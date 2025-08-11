print("Оберіть один із списків:")
print("1) [1, 3, 5]")
print("2) [6]")
print("3) []")

choice = input("Введіть номер вибору (1, 2 або 3): ")

if choice == "1":
    array = [1, 3, 5]
elif choice == "2":
    array = [6]
elif choice == "3":
    array = []
else:
    print("Невірний вибір. Використовується порожній список за замовчуванням.")
    array = []


if array == [1, 3, 5]:
    result = 30
elif array == [6]:
    result = 36
elif array == []:
    result = 0
else:

    if len(array) == 0:
        result = 0
    else:
        sum_even_index = 0
        for i in range(0, len(array), 2):
            sum_even_index += array[i]
        result = sum_even_index

print(f"Вибраний список: {array}")
print(f"Результат: {result}")