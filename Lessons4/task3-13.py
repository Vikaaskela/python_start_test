#Task 3
#Напишіть скрипт, який виводить цілі числа від 1 до 200, використовуючи цикл while. 
#В одному рядку необхідно виведити лише п’ять цілих чисел.
#Наприклад,
#1 2 3 4 5
#6 7 8 9 10
#11 12 13 14 15
i = 1
while i <= 200:
    print(i, end=' ')
    if i % 5 == 0:
        print()
    i += 1