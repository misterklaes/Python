import random

random_list = []
length = random.randint(3, 10)

for i in range(length):
    random_list.append(random.randint(1, 100))

print("Початковий список:", random_list)
print("Довжина списку:", len(random_list))

new_list = []
new_list.append(random_list[0])
new_list.append(random_list[2])
new_list.append(random_list[-2])

print("Новий список:", new_list)