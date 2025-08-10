list1 = [0, 1, 0, 12, 3]
list2 = [0]
list3 = [1, 0, 13, 0, 0, 0, 5]
list4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

print("Список 1:", list1)
print("Список 2:", list2)
print("Список 3:", list3)
print("Список 4:", list4)

print("Виберіть один із списків (введіть число 1, 2, 3 або 4):")
choice = input()

if choice == "1":
    nums = list1
elif choice == "2":
    nums = list2
elif choice == "3":
    nums = list3
elif choice == "4":
    nums = list4
else:
    print("Ви ввели неправильний номер")
    nums = []

if len(nums) > 0:
    new_list = []
    
    for i in range(len(nums)):
        if nums[i] != 0:
            new_list.append(nums[i])
    
    zeros_count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zeros_count = zeros_count + 1
    
    for i in range(zeros_count):
        new_list.append(0)
    
    print("Результат:", new_list)