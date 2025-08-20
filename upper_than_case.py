user_input = input("Введіть строку: ")
hash_tag = "#"
title_user_input_string = user_input.title()
remove_user_input_spaces = title_user_input_string.replace(" ", "")
truncate_user_stringto_140_signs = remove_user_input_spaces[:140]
print(f"'{hash_tag}{truncate_user_stringto_140_signs}'")