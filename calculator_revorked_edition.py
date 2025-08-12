while True:
    print("Калькулятор!")
    a = int(input("Перше число: "))
    b = int(input("Друге число: "))
    sign = input("Що робити? (+ - * /): ")
    
    if sign == "+":
        print(a + b)
    if sign == "-":
        print(a - b)
    if sign == "*":
        print(a * b)
    if sign == "/":
        if b == 0:
            print("Не можна ділити на 0!")
        else:
            print(a / b)
    if sign not in ["+", "-", "*", "/"]:
        print("Неправильний знак!")
    
    again = input("Ще? (yes/y/n): ")
    if again not in ["yes", "y"]:
        break