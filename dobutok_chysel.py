def multiply_digits_until_single_digit(number):
    current_number = number
    count = 0
    while current_number >= 10:
        print(f"Поточне число: {current_number}")
        number_as_string = str(current_number)
        product_of_digits = 1
        for digit_char in number_as_string:
            digit_int = int(digit_char)
            product_of_digits = product_of_digits * digit_int
        current_number = product_of_digits
        print(f"Добуток цифр: {current_number}")
        count = count + 1

    print(f"Кінцевий результат: {current_number}")
    print(f"Кількість ітерацій: {count}")
    return current_number
user_input = input("Введіть число: ")
multiply_digits_until_single_digit(user_input)
