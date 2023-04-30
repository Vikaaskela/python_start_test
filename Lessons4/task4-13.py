#Task 4
#Напишіть скрипт, який обчислює за допомогою циклу факторіал числа n (n вводиться з клавіатури).
n = int(input('n='))
fact = 1
for i in range(2, n + 1):
    fact  = fact *i
print(fact )