#Write your code here.
import locale
numbers = input().split(",")
numbers = [str(num) for num in numbers]
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
for i in range(len(numbers)):
    numbers[i] = locale.format("%d", int(numbers[i]), grouping=True)
print(numbers)
