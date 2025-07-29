user_number = int(input("Введіть число, яке складається із 5-ох знаків: "))
l1 = user_number // 10000
l2 = (user_number // 1000) % 10
l3 = (user_number // 100) % 10
l4 = (user_number // 10  ) % 10
l5 = user_number % 10
print(l5 * 10000 + l4 * 1000 + l3 * 100 + l2 * 10 + l1)