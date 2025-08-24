seconds = int(input("Введіть число секунд (0 ≤ N < 8640000): "))
days, rem = divmod(seconds, 24 * 60 * 60)
hours, rem = divmod(rem, 60 * 60)
minutes, secs = divmod(rem, 60)
if days % 10 == 1 and days % 100 != 11:
    day_word = 'день'
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word = 'дні'
else:
    day_word = 'днів'
time_str = f"{hours:02}:{minutes:02}:{secs:02}"
print(f"{days} {day_word} {time_str}")
