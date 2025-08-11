print("Оберіть один із списків або введіть свій власний:")
print("1) [1, 3, 5]")
print("2) [6]")
print("3) []")
print("4) Ввести власний список")

choice = input("Введіть номер вибору (1, 2, 3 або 4): ")

# Визначаємо вхідний масив залежно від вибору користувача
if choice == "1":
    array = [1, 3, 5]
elif choice == "2":
    array = [6]
elif choice == "3":
    array = []
elif choice == "4":
    # Користувач вводить свій список
    print("Введіть числа через пробіл (наприклад: 1 2 3 4):")
    user_input = input()
else:
    print("Невірний вибір. Використовується порожній список за замовчуванням.")
    array = []

print(f"Вибраний список: {array}")

# Обробка результату залежно від списку
if len(array) == 0:
    # Для порожнього масиву результат завжди 0
    result = 0
    print("Список порожній, результат = 0")
else:
    # Знаходимо суму елементів з парними індексами
    sum_even_indices = 0
    for i in range(0, len(array), 2):  # Починаємо з 0, крок 2 (парні індекси)
        sum_even_indices += array[i]
    last_element = array[-1]
    result = sum_even_indices * last_element

    print(f"Результат: {sum_even_indices} * {last_element} = {result}")