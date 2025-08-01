print("Программа калькулятор запитує по черзі Число А, Число Б та математичну дію")
a = int(input("Введіть Число А: "))
b = int(input("Введіть Число Б: "))
calculation_sign = input("Введіть знак математичної дії: ")
if calculation_sign == "+":
    print(a + b)
elif calculation_sign == "-":
    print(a - b)
elif calculation_sign == "*":
    print(a * b)
elif calculation_sign == "/":
    if b != 0:
        print(a / b)
    else:
        print("Ділення на нуль неможливе")
else:
    print("Невідома математична дія")