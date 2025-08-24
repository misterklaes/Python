import string
user_input = input("Введіть два символи через дефіс (наприклад A-Z): ").strip()
first_letter, last_letter = user_input.split('-')
all_letters = string.ascii_letters
start_index = all_letters.index(first_letter)
last_index = all_letters.index(last_letter)
result = all_letters[start_index:last_index + 1]
print(result)