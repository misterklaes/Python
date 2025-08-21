name = input("Введіть назву змінної: ").strip()

if not name:
    print("Назва порожня – це недійсне ім’я.")
elif name[0].isdigit():
    print("Невірно: починається з цифри.")

else:
    if any(ch.isupper() for ch in name):
        print("Невірно: містить великі літери.")

    else:
        punctuation = "!\"#$%&'()*+,-./:;<=>?@[\$^`{|}~"
        if any(ch in punctuation or ch.isspace() for ch in name):
            print("Невірно: містить заборонені символи (пробіл чи пунктуацію).")

        else:
            reserved = {
                "and", "as", "assert", "break", "class",
                "continue", "def", "del", "elif", "else",
                "except", "False", "finally", "for", "from",
                "global", "if", "import", "in", "is", "lambda",
                "None", "nonlocal", "not", "or", "pass",
                "raise", "return", "True", "try", "while",
                "with", "yield"
            }
            if name in reserved:
                print("Невірно: назва є зареєстрованим словом.")
            else:
                print("Назва дійсна – відповідає всім правилам.")